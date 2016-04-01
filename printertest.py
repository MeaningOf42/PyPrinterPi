#!/usr/bin/python

from Adafruit_Thermal import *

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)

printer.println("Testing...")
printer.println("If you're seeing this it works")
printer.println("the final version should look something like this: ")
printer.println("the final version should look something like this: ")
printer.println("3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679")
printer.println("Here's an empty space made with blank lines:")
printer.println("")
printer.println("")
printer.println("Done")