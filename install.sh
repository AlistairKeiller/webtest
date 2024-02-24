#!/bin/sh
mkdir -p "/Applications/Adobe Connect Dark Mode.app/Contents/MacOS"
echo """#!/bin/sh
/Applications/Adobe\ Connect/Adobe\ Connect.app/Contents/MacOS/Adobe\ Connect --remote-debugging-port=9222""" > "/Applications/Adobe Connect Dark Mode.app/Contents/MacOS/Adobe Connect Dark Mode"
chmod +x "/Applications/Adobe Connect Dark Mode.app/Contents/MacOS/Adobe Connect Dark Mode"
