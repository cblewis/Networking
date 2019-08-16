#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import time

#Masterfully crafted by Cameron Lewis

#Specify the device type:
mrv = {
    "host": input("IP: "),
    "username": input("Username: "),
    "password": getpass(),
    "device_type": "mrv_optiswitch",
    'global_delay_factor': 2,
}

confip = input("172.22.6.X address to be assigned to this device: ")
#enablepass = input("Enable password: ")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Specify the device type here too:
net_connect = Netmiko(**mrv)

#See if enable password is required.
login = net_connect.find_prompt()
print(login)
if r"Password" in login:
    try:
        print(net_connect.find_prompt())
        #output = net_connect.send_command(enablepass + r"\\n")
        output = net_connect.send_command("jobbob" + r"\\n")
        print(output)
    except:
        raise
elif r">" in login:
    try:
        print(net_connect.find_prompt())
        output = net_connect.send_command("enable", expect_string=r'>')
        print(output)
        print(net_connect.find_prompt())
        #output = net_connect.send_command(enablepass + r"\\n")
        output = net_connect.send_command("jobbob" + r"\\n")
        print(output)
    except:
        raise
else:
    print("No need for enable password.")

print(net_connect.find_prompt())
output = net_connect.send_command("conf t", expect_string=r'#')
print(output)

#Specify from which file commands will be read
filepath = 'config.txt'
with open(filepath, 'r') as f:
    configLines = f.readlines()
    for line in configLines:
        print(net_connect.find_prompt())
        print(line)
        output = net_connect.send_command(line, expect_string=r'#')
        print(output)
        #time.sleep(4)
f.close()

#Configure new MGMT IP on device
mgmtcommand = "ip " + confip + "/22"
print(net_connect.find_prompt())
print(mgmtcommand)
output = net_connect.send_command(mgmtcommand, expect_string=r'#')
print(output)

#Save Changes
savemem = "wr mem"
print(net_connect.find_prompt())
print(savemem)
output = net_connect.send_command(savemem, expect_string=r'#')
print(output)

#Logout from the SSH connection.
net_connect.disconnect()
