#Masterfully crafted by Cameron Lewis
'''
#If a single MAC is just plain characters:
str = 'Ffffffffffff'
newstr = ':'.join(str[i:i+2] for i in range(0, len(str), 2))
print(newstr)
'''

#If MAC addresses are legion and in a text file:
with open ('macaddresses.txt', 'r') as macfile:
    for item in macfile:
        str = item
        newstr = ':'.join(str[i:i+2] for i in range(0, len(str), 2))
        print(newstr)

with open ('macaddresses.txt', 'r') as macfile:
    for item in macfile:
        str = item
        if ':' in str:
            nocharstring = str.replace(":", "")
        elif '-' in str:
            nocharstring = str.replace("-", "")
        print(nocharstring)

'''
#If MAC address is formatted with '.':
str = 'Ffff.ffff.ffff'
nocharstring = str.replace(".", "")
newstr = ':'.join(nocharstring[i:i+2] for i in range(0, len(nocharstring), 2))
print(newstr)
'''

'''
#If MAC address is formatted with '-' every two characters:
str = 'Ffff.ffff.ffff'
nocharstring = str.replace("-", "")
newstr = ':'.join(nocharstring[i:i+2] for i in range(0, len(nocharstring), 2))
print(newstr)
'''

'''
#If MAC address is formatted with '-' every four cahracters:
str = 'Ffff-ffff-ffff'
nocharstring = str.replace("-", "")
newstr = ':'.join(nocharstring[i:i+4] for i in range(0, len(nocharstring), 4))
print(newstr)
'''
