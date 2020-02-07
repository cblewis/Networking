#!/usr/bin/env python
import serial
import time
from getpass import getpass

#Masterfully crafted by Cameron Lewis

#check devmngr for serial port and its settings
console = serial.Serial(
    port="COM3",
    baudrate="9600",
    parity="N",
    stopbits=1,
    bytesize=8,
    timeout=8
)

#Specify config script here
filepath = 'SERIALscript_config_ciena3930.txt'

print("Is " + filepath + " the correct config file that you want to use?")
option = input("Type yes to continue: ")
if "yes" not in option:
    exit()

username = input("Username: ")
password = getpass()
#need to convert the input of these variables as bytes
nameb = bytes(username, encoding= "utf-8")
passb = bytes(password, encoding= "utf-8")

console.write(b'\n')
time.sleep(1)
input_data = console.read(console.inWaiting())
print(input_data)

console.write(nameb)
console.write(b'\n')
#console.write("b'" + username + "\n'" + "b'\n'").encode() doesnt work
time.sleep(1)
input_data = console.read(console.inWaiting())
print(input_data)

console.write(passb)
console.write(b'\n')
#console.write("b'" + password + "\n'" + "b'\n'").encode() doesnt work
time.sleep(2)
input_data = console.read(console.inWaiting())
print(input_data)

console.write(b'\n')
time.sleep(1)
input_data = console.read(console.inWaiting())
print(input_data)

print("Please wait for 15 seconds before the configuration begins.")
time.sleep(14)

console.write(b'\n')
time.sleep(1)
input_data = console.read(console.inWaiting())
print(input_data)

#if we read as bytes 'rb', then we don't have to concatenate
#every line in the config with b'line'\n like appendconfig.py
with open(filepath, 'rb') as f:
    configLines = f.readlines()
    for line in configLines:
        print(line)
        console.write(line)
        #console.write(b'\n')
        input_data = console.read(console.inWaiting())
        print(input_data)
        time.sleep(1)
f.close()

console.write(b'exit' + b'\n')
input_data = console.read(console.inWaiting())
print(input_data)

exit()
