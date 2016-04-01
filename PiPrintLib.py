from decimal import *
import os

def gauss_pi_method(decimals):
    getcontext().prec = decimals+10 #sets precision to 10 more decimal places than asked for.
    pi = 4*(12*arctan(18) + 8*arctan(57) - 5*arctan(239))
    
    getcontext().prec = decimals #this block of code rounds pi to the number of decimal places asked for
    pi = +pi

    f = open('pi.txt', 'w') #this block saves our value of pi to pi.txt
    f.write(str(pi))
    f.close()
    return

def arctan(x):
    
    one=10**getcontext().prec
    
    xSquaredPlusOne = (x*x) + 1
    fract = (x * one) // xSquaredPlusOne
    total = fract
    numurator_num = 2
    while 1:
        denominator = (numurator_num+1) * xSquaredPlusOne
        fract *= numurator_num
        fract = fract // denominator
        if fract == 0:
            break
        total += fract
        numurator_num += 2
    return Decimal(Decimal(total)/Decimal(one))

def printer_print(string): #this function saves a string to a text file then uses a python 2 program to print it
    f = open('passtopython2.txt', 'w') #this block saves our value of pi to pi.txt
    f.write(string)
    f.close()
    os.system("python printfrom3.py")
    return

def pi_cheat(decimals): #this function is used to change pi.txt to a value of pi correct to the number of places asked for without having to calculate pi
    f = open('pi_cheat.txt', 'r') #This block opens pi.txt and saves its contents as a string
    pi_cheat = f.read()
    f.close()
    if decimals>len(pi_cheat):
        p = open('pi.txt', 'w') #this block saves our value of pi to pi.txt
        p.write(str(pi_cheat))
        p.close()
    else:
        p = open('pi.txt', 'w') #this block saves our value of pi to pi.txt
        p.write(str(pi_cheat[:decimals]))
        p.close()
    return

def printpi():
    os.system("sudo python printpi.py")
