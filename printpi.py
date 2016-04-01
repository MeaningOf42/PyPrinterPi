#!/usr/bin/python
from Adafruit_Thermal import *

pi_leg_length = 9

f = open('pi.txt', 'r')
pi = f.read()
f.close()

pi_formatted = ""
count = 1
for i in pi:
    if count<32:
        pi_formatted +=i
        
    elif count == ((2*pi_leg_length) + 31):
        pi_formatted += "                   " + i
        
    elif count%2:
        pi_formatted += "                 " + i

    elif count == ((2*pi_leg_length) + 30):
        pi_formatted += "\n     " + i
        
    elif count == ((2*pi_leg_length) + 32):
        pi_formatted += "\n \ n \n" + i
        count = 1
        
    else:
        pi_formatted += "\n      " + i 
        

    count += 1

pi_line_split = pi_formatted.spli("\n")

for i in pi_line_split:
    printer.println(i)
