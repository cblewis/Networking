#!/usr/bin/env python
from netmiko import Netmiko
from getpass import getpass
import time

#Masterfully crafted by Cameron Lewis

#Specify the device type:
ciena = {
    "host": input("IP: "),
    "username": input("Username: "),
    "password": getpass(),
    "device_type": "ciena_saos",
    #"global_delay_factor": 2,
}

confip = input("172.22.4.X address to be assigned to this device: ")
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#Specify the device type here too:
net_connect = Netmiko(**ciena)

#time.sleep(10)

print(net_connect.find_prompt())
output = net_connect.send_command('\n', expect_string=r'>')
print(output)

#Specify from which file commands will be read
filepath = '3930 reprovision conf.txt'
with open(filepath, 'r') as f:
    configLines = f.readlines()
    for line in configLines:
        print(net_connect.find_prompt())
        print(line)
        output = net_connect.send_command(line, expect_string=r'>')
        print(output)
        #time.sleep(4)
f.close()
'''
filepath2 = '3930snmp.txt'
with open(filepath2, 'r') as f2:
    configLines2 = f2.readlines()
    for line2 in configLines2:
        print(net_connect.find_prompt())
        print(line2)
        output = net_connect.send_command_timing(line2, strip_command=False, strip_prompt=False)
        print(output)
        time.sleep(2)
f2.close()
'''
#Configure new MGMT IP on device
mgmtcommand = "interface remote set ip " + confip + "/22 vlan 256 gateway 172.22.4.1"
print(net_connect.find_prompt())
print(mgmtcommand)
output = net_connect.send_command(mgmtcommand, expect_string=r'>')
print(output)

#Save Changes
savemem = "conf save"
print(net_connect.find_prompt())
print(savemem)
output = net_connect.send_command(savemem, expect_string=r'>')
print(output)

#Logout from the SSH connection.
net_connect.disconnect()
