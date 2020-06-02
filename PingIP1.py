#!/user/bin/env Python
#Masterfully crafted by Cameron Lewis

import subprocess

with open('iplist.txt', 'r') as ipfile:
    for ip in ipfile:
        with open('pingresult.txt', 'a') as pingfile:
            command1 = subprocess.run(['ping -c 4 ' + ip], stdout=pingfile, shell=True)
            print(command1)
