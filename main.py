#import dependancies
import RPi.GPIO as GPIO
import time
import PiPrintLib
#set up gpio correctly
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(25,GPIO.IN)

#set up names for buttons, used for talking to user
button1_name = "*"
button2_name = "7"
button3_name = "#"

#This block of code ask user if they want to cheat
PiPrintLib.printer_print("Do you want to cheat")
PiPrintLib.printer_print("and use values")
PiPrintLib.printer_print("from pi_cheat.txt?\n")
PiPrintLib.printer_print("")
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you cheat you won't")
PiPrintLib.printer_print("calculate pi,")
PiPrintLib.printer_print("just print it.")
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you want to cheat,")
PiPrintLib.printer_print("press " + button1_name)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you want to calculate,")
PiPrintLib.printer_print("press " + button2_name)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("")

cheat = 0 #value for whether or not user wants to cheat

while True: #This loop waits for the user to select wheather or not the want to cheat
    if (GPIO.input(23)):
        PiPrintLib.printer_print("You chose to cheat")
        cheat = 1
        break
    if (GPIO.input(24)):
        PiPrintLib.printer_print("You chose to calculate")
        break

PiPrintLib.printer_print("")

decimal_power_of_ten = 4 #a value for how many places of pi the user wants printing

PiPrintLib.printer_print("You will now select")
PiPrintLib.printer_print("how many places of pi")
PiPrintLib.printer_print("you want printed.")
PiPrintLib.printer_print("You can only chose")
PiPrintLib.printer_print("a power of ten.")

updated = 1 #variable used for the next loop. Is used to check whether or not a button has been pressed since the last iteration

while True: #This loop waits for the user to the number of digits of pi they want to print out.
    if updated == 1:
        #this block of code asks the user what they want to do
        PiPrintLib.printer_print("This program")
        PiPrintLib.printer_print("is currently set")
        PiPrintLib.printer_print("to print 10^" + str(decimal_power_of_ten) + "digits of pi")                     
        PiPrintLib.printer_print("To increase")
        PiPrintLib.printer_print("the power by 1:")
        PiPrintLib.printer_print("Press " + button3_name)
        PiPrintLib.printer_print("")
        PiPrintLib.printer_print("To decrease")
        PiPrintLib.printer_print("the power by 1:")
        PiPrintLib.printer_print("Press " + button1_name)
        PiPrintLib.printer_print("")
        PiPrintLib.printer_print("To run the program:")
        PiPrintLib.printer_print("Press " + button2_name)
        PiPrintLib.printer_print("")
        PiPrintLib.printer_print("")
        updated = 0
    
    if (GPIO.input(23)):
        decimal_power_of_ten -= 1
        updated = 1
        if decimal_power_of_ten<1:
            PiPrintLib.printer_print("You can't go that low.")
            decimal_power_of_ten = 1
        
    if (GPIO.input(25)):
        decimal_power_of_ten += 1
        updated = 1
        if decimal_power_of_ten>6:
            PiPrintLib.printer_print("You can't go that high.")
            decimal_power_of_ten = 6

    if (GPIO.input(24)):
        break

start_time = time.time()

if cheat:
    PiPrintLib.pi_cheat(10**decimal_power_of_ten)
else:
    PiPrintLib.gauss_pi_method(10**decimal_power_of_ten)

end_time = time.time()

PiPrintLib.printer_print("Pi was just calculated in:")
PiPrintLib.printer_print("%s seconds" % (time.time() - start_time))
PiPrintLib.printer_print("")
PiPrintLib.printer_print("Pi to " + str(10**decimal_power_of_ten) + "decimal places is")
PiPrintLib.printpi()

