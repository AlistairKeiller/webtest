import requests
import json
import websocket
import time

def inject_dark_mode(debugger_url):
    try:
        response = requests.get(debugger_url)
        pages = response.json()

        for page in pages:
            page_id = page['id']
            ws_url = page['webSocketDebuggerUrl']

            # JavaScript code to inject DarkReader into the first iframe's head
            js_code = """
                var iframes = document.getElementsByTagName('iframe');
                if (iframes.length > 0) {
                    var iframeHead = iframes[0].contentWindow.document.head;
                    var script = document.createElement('script');
                    script.src = 'https://unpkg.com/darkreader@4.9.73/darkreader.js';
                    script.onload = function() {
                        iframes[0].contentWindow.DarkReader.enable({darkSchemeBackgroundColor: "#1e1e2e", darkSchemeTextColor: "#cdd6f4", selectionColor: "#585b70"});
                    };
                    iframeHead.appendChild(script);
                }
            """

            command = json.dumps({
                "id": 1,
                "method": "Runtime.evaluate",
                "params": {
                    "expression": js_code,
                    "awaitPromise": True
                }
            })

            ws = websocket.create_connection(ws_url)
            ws.send(command)
            response = ws.recv()
            print(f"Injected DarkReader into iframe for page ID {page_id}: {response}")
            ws.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Inject DarkReader into iframes in a loop
while True:
    inject_dark_mode("http://localhost:9222/json")
    time.sleep(1)
