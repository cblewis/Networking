#!/user/bin/env Python
#Masterfully crafted by Cameron Lewis

import subprocess
from subprocess import PIPE

with open('iplist.txt', 'r') as ipfile:
    for ip in ipfile:
        with open('pingresult.txt', 'a') as pingfile:
            command1 = subprocess.run(['ping -c 4 ' + ip], stdout=PIPE, stderr=PIPE, shell=True)
            pingfile.write(command1.stdout.decode())
            print('If the following line is blank, there are no errors.')
            print(command1.stderr.decode())
            if command1.returncode != 0
                print(There was an error:)
                print(command1.returncode.decode())
                break
    print("Job's done.")
