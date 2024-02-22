import requests
import json
import websocket

debugger_url = "http://localhost:9222/json"

response = requests.get(debugger_url)
pages = response.json()

if pages:
    page_id = pages[0]['id']
    ws_url = pages[0]['webSocketDebuggerUrl']

    js_code = """
        var script = document.createElement('script');
        script.onload = function() {
            DarkReader.enable();
        };
        script.src = 'https://unpkg.com/darkreader@4.9.77/darkreader.js';
        document.body.appendChild(script);
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
    print(f"Inject script command sent for page ID {page_id}, response: {ws.recv()}")
    ws.close()
else:
    print("No pages found")
