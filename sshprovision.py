#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import time

#Masterfully crafted by Cameron Lewis

#Specify the device type:
ciena = {
    "host": input("IP: "),
    #"host": "10.0.0.92",
    "username": input("Username: "),
    "password": getpass(),
    "device_type": "ciena_saos",
}
'''
mrv = {
    "host": "192.168.1.14", #10.0.0.139
    "username": input("Username: "),
    "password": getpass(),
    "device_type": "mrv_optiswitch",
}
'''

#Specify the device type here too:
net_connect = Netmiko(**ciena)

#Specify from which file commands will be read
filepath = 'config.txt'
with open(filepath, 'r') as f:
    configLines = f.readlines()
    for line in configLines:
        print(net_connect.find_prompt())
        print(line)
        output = net_connect.send_command(line)
        print(output)
        print()
        time.sleep(4)
f.close()

#Logout from the SSH connection.
command = 'exit'
print()
print(net_connect.find_prompt())
output = net_connect.send_command(command)
print(output)
print()
net_connect.disconnect()
exit
