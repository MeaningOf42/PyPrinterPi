#import dependancies
import RPi.GPIO as GPIO
import time
import PiPrintLib
#set up gpio correctly
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)
GPIO.setup(24,GPIO.IN)
GPIO.setup(23,GPIO.IN)

#set up names for buttons, used for talking to user
button1_name = "*"
button2_name = "0"
button3_name = "#"

#This block of code ask user if they want to cheat
PiPrintLib.printer_print("Do you want to cheat")
PiPrintLib.printer_print("and use values")
PiPrintLib.printer_print("from pi_cheat.txt?\n")
PiPrintLib.printer_print("")
time.sleep(0.2)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you cheat you won't")
PiPrintLib.printer_print("calculate pi,")
PiPrintLib.printer_print("just print it.")
time.sleep(0.2)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you want to cheat,")
PiPrintLib.printer_print("press " + button1_name)
time.sleep(0.2)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you want to calculate,")
PiPrintLib.printer_print("press " + button2_name)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("")

while True:
    if (GPIO.input(23)):
        PiPrintLib.printer_print("You chose to cheat")
        break
    if (GPIO.input(24)):
        PiPrintLib.printer_print("You chose to calculate")
        break
    
