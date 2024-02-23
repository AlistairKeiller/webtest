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

            js_code = """
                if (typeof DarkReader === 'undefined') {
                    var script = document.createElement('script');
                    script.onload = function() {
                        DarkReader.enable();
                        document.body.setAttribute('darkreader-injected', 'true');
                    };
                    script.src = 'https://unpkg.com/darkreader@4.9.77/darkreader.js';
                    document.body.appendChild(script);
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
            response = ws.recv()  # Receive server response
            print(f"Injected DarkReader for page ID {page_id}: {response}")
            ws.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Continuous service loop
while True:
    inject_dark_mode("http://localhost:9222/json")
    time.sleep(1)  # Wait for 60 seconds before checking again
