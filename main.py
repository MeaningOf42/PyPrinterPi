#import dependancies
import RPi.GPIO as GPIO
import time
import PiPrintLib
#set up gpio correctly
GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.IN)

#set up names for buttons, used for talking to user
button1_name = "*"
button2_name = "0"
button3_name = "#"

#
PiPrintLib.printer_print("Do you want to cheat and use values from pi_cheat.txt?")
PiPrintLib.printer_print("")
time.sleep(0.2)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you cheat you won't calculate pi, just print it")
time.sleep(0.2)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you want to cheat press " + button1_name)
time.sleep(0.2)
PiPrintLib.printer_print("")
PiPrintLib.printer_print("If you want to calculate press " + button2_name)
