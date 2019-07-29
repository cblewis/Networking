# Networking Scripts


Serial Provisioning

This script prompts for a username and password, then opens and reads commands from a separate text 
file and writes them to the device over a serial connection. This minimizes user error when copying 
and pasting commands to provision routers, switches, or other devices and inputs the commands faster 
than what can be typed by human hands.


SSH Provisioning 

This script prompts for a username and password, then opens and reads commands from a separate text 
file and writes them to the device over an SSH connection. Like my serial provisioning script, this 
minimizes user error when copying and pasting commands to provision routers, switches, or other 
devices and inputs the commands faster than what can be typed by human hands.
The modules in this script rely on specifying the device type before an SSH connection can be 
established.


UDP Socket & Client

These are scripts that I made to mimic UDP and TCP clients and server connections. 
The client sends a lowercase message to the server, which returns that same message capitalized. 

