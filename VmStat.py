import subprocess
from subprocess import PIPE

cmd1 = subprocess.run(['vmstat'], stdout=PIPE, shell=True)
cmd2 = cmd1.stdout.decode().split('\n')
cmddict = dict(zip(cmd2[1].split(), cmd2[2].split()))

print(cmd2)
print(cmddict)

if int(cmddict['free']) < 100:
    print('Need more space!')
elif int(cmddict['free']) > 100:
    print('We have sufficient space.')
