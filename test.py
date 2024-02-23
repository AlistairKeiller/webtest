import requests
import json
import websocket
import time

def inject_dark_mode(debugger_url, css_content):
    try:
        response = requests.get(debugger_url)
        pages = response.json()

        for page in pages:
            page_id = page['id']
            ws_url = page['webSocketDebuggerUrl']

            js_code = f"""
                if (!document.getElementById('customDarkStyle')) {{
                    var style = document.createElement('style');
                    style.type = 'text/css';
                    style.id = 'customDarkStyle';  // Unique ID for the style element
                    style.innerHTML = `{css_content}`;
                    document.getElementsByTagName('head')[0].appendChild(style);
                }}
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
            print(f"Injected custom CSS for page ID {page_id}: {response}")
            ws.close()
    except Exception as e:
        print(f"An error occurred: {e}")

# Load the CSS file content
css_file_path = 'DarkReader-pcadobeconnect-stanford-edu.css'
with open(css_file_path, 'r') as file:
    css_content = file.read().replace('\n', '\\n')

# Inject CSS in a loop
while True:
    inject_dark_mode("http://localhost:9222/json", css_content)
    time.sleep(1)
