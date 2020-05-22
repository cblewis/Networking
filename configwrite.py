
#Masterfully crafted by Cameron

with open ("template.txt", "r") as templatefile:
    readtemplate = templatefile.readlines()

with open ('2400config.txt', 'w') as finalfile:
    for line in readtemplate:
        if line[0].isdigit():
            pass
#I chose to pass this if statement and not write it rather than write !,
#which would comment out the line when it is being passed to a network configuration
            #finalfile.write("!")
            #finalfile.write(line)
        else:
            finalfile.write(line)
'''
#alternate way to check for the beginning of a line
    for line in readtemplate:
        if line.startswith(('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')):
#startswith requires an entire tuple to be passed to it to check
            pass
            #finalfile.write("!")
        else:
            finalfile.write(line)
'''
templatefile.close()
finalfile.close()
