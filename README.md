# How to install
```bash
bash install.sh
```
# How to uninstall
```bash
bash uninstall.sh
```
# Basic overview
It will create a new application, name Adobe Connect Dark Mode, that launch the Adobe Connect application with a remote debug port. Then, it will run a Python script in the background that tries to connect to that debug port using the Chrome dev tools protocol. If it connects, then it will inject the darkreader javascript with the catppuccin mocha theme. It prefers to inject into the head of an iframe (since that is the primary mechanism that Adobe Connect uses to display meetings), but if it can't find an iframe, it will inject it into the head of the document. It will repeat this attempted injection process every second, running in the background as a launchctl task. The uninstall script will remove the Adobe Connect Dark Mode application wrapper and the launchctl task.
