# This a program developed by Billy Timimi that prints out the value of pi in
# the shape of pi. Thanks to Adafruit for providing the Thermal_Printer library,
# which made this program possible. The original library is availible at:
# https://github.com/adafruit/Python-Thermal-Printer/blob/master/Adafruit_Thermal.py
#

#!/usr/bin/python
from Adafruit_Thermal import * #import's Adafruit's library

pi_leg_length = 9 #defines how many digits tall pi's legs should be.

f = open('pi.txt', 'r') #This block opens pi.txt and saves its contents as a string
pi = f.read()
f.close()

pi_formatted = "" #pi_formatted is used to contain a formatted version of pi, it will eventually contain the contents of pi in the shape of
                  #multiple pi symbols

count = 1 #count variable is used to place characters from pi into pi_formatted with the right spacings

for i in pi: #this loops through all the digits of pi (the variable not the number).
             #count variable increases to 50 then drops to 1, each time it reaches 49 a new pi symbol is completed

    if count<32:            #the first 31 characters of the pi symbol are placed next to each other creating the line at the top
        pi_formatted +=i
        
    elif count == ((2*pi_leg_length) + 31):         #skip this comment until you've undstood how the legs of pi are created,
        pi_formatted += "                   " + i   #adds two extra spaces before the last character of the pi symbol in order to create the outwards
                                                    #curve on the right leg of the pi symbol.
        
    elif count%2:                                   #if count is an odd number, adds spacing then the character, this creates the right leg of the pi 
        pi_formatted += "                 " + i     #symbol

    elif count == ((2*pi_leg_length) + 30):         #skip this comment until you've undstood how the legs of pi are created,
        pi_formatted += "\n     " + i               #creats a new line and spacing before the second to last character of the pi symbol, there is one less
                                                    #space in the spacing, this creates the leftwards curve on the left leg 
        
    elif count == ((2*pi_leg_length) + 32):         #On the 50th character create a new pi symbol by adding three line breaks, adding the character 
        pi_formatted += "\n \n \n" + i              # then returning count to one
        count = 1
        
    else:                                           #If none of the above elif statement's applied then 48>count>31 and count is even. If this is the case
        pi_formatted += "\n      " + i              #the character should be used to to make the left leg of the pi symbol. It does this by creating a new line
                                                    #then adding spacing
        

    count += 1 #increments the count variable

#if the loop above doesn't make sense to you try thinking about how it would run when the program is executed.

pi_line_split = pi_formatted.split("\n") #creates a list of all the lines in pi_formatted

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5) #this line sets up the printer

printer.println("pi =") #This print the line pi=
printer.println("3.14159265358979323846264338327") #for some reason the first line of pi_line_split doesn't print on it's own so I'm printing it manually

for i in pi_line_split:
    printer.println(i) #prints every line in pi_line_split

printer.println("") #prints a couple of blank lines in order to show all of the print
printer.println("")
