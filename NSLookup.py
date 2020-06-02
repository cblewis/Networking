#!/user/bin/env Python
#Masterfully crafted by Cameron Lewis

import subprocess

with open('iplist.txt', 'r') as ipfile:
    for ip in ipfile:
        with open('nsresult.txt', 'a') as dnsfile:
            subprocess.run(['nslookup ' + ip], stdout=dnsfile, shell=True)
