#!/usr/bin/python

from Adafruit_Thermal import * #imports Adafruits_library
import os

f = open('passtopython2.txt', 'r') #This block opens passtopython2.txt and saves its contents as a string
string = f.read()
f.close()

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5) #creates printer object

printer.println(str(string))
os.system("rm passtopython2.txt")
