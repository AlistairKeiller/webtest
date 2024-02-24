#!/bin/sh
mkdir -p "/Applications/Adobe Connect Dark Mode.app/Contents/MacOS"
echo """#!/bin/sh
/Applications/Adobe\ Connect/Adobe\ Connect.app/Contents/MacOS/Adobe\ Connect --remote-debugging-port=9222""" > "/Applications/Adobe Connect Dark Mode.app/Contents/MacOS/Adobe Connect Dark Mode"
chmod +x "/Applications/Adobe Connect Dark Mode.app/Contents/MacOS/Adobe Connect Dark Mode"
echo """<?xml version=\"1.0\" encoding=\"UTF-8\"?>
<!DOCTYPE plist PUBLIC \"-//Apple//DTD PLIST 1.0//EN\" \"http://www.apple.com/DTDs/PropertyList-1.0.dtd\">
<plist version=\"1.0\">
<dict>
    <key>Label</key>
    <string>com.alistair.webtest</string>
    <key>ProgramArguments</key>
    <array>
        <string>/usr/bin/python3</string>
        <string>$(pwd)/test.py</string>
    </array>
    <key>RunAtLoad</key>
    <true/>
    <key>KeepAlive</key>
    <true/>
    <key>StandardErrorPath</key>
    <string>/tmp/com.alistair.webtest.err</string>
    <key>StandardOutPath</key>
    <string>/tmp/com.alistair.webtest.out</string>
</dict>
</plist>""" > com.alistair.webtest.plist
launchctl load com.alistair.webtest.plist
