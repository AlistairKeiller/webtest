#!/bin/sh
rm -r "/Applications/Adobe Connect Dark Mode.app"
rm ~/Library/LaunchAgents/com.alistair.webtest.plist
launchctl ~/Library/LaunchAgents/com.alistair.webtest.plist
