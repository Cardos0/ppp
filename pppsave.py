import serial
import os

ser = serial.Serial('/dev/pts/2')
filename = 'ppp.txt'

os.system('rm ' + filename)
os.system('cls||clear')
f = open (filename, 'w')

while(True):
    r_byte = ser.read()
    f.write(r_byte)
    f.flush()