from decimal import *
import time

def gauss_pi_method():
    return 4*(12*arctan(18) + 8*arctan(57) - 5*arctan(239))

def arctan(x): #defins a function for defining pi using the formula we derived
    
    acuracy = Decimal(Decimal(1)/Decimal(10**(getcontext().prec-3)))
    xSquaredPlusOne= Decimal(x**2 + 1)
    result = Decimal(Decimal(x)/Decimal(xSquaredPlusOne)) #result is a variable used to store our current value of pi as a decimal, 1 and x are turned into  decimals to avoid rounding errors
    fract = result
    numurator_num = 2 # even num is used to multiplie the denominator
    denominator_num = 3
    
    while True:
        fract = (fract*numurator_num)/(Decimal(denominator_num)*xSquaredPlusOne)
        result += fract
        if fract<acuracy:
            break
        numurator_num += 2
        denominator_num += 2

    return result

while 1:
    #Ask's the user how many decimal places they want there answer to be given to
    decimals = int(input("Enter how many decimal places do you want the answer to be given to: "))+1
    start_time = time.time()
    getcontext().prec = decimals+4 #sets precision to 4 more decimal places than asked for.
    
    PiEst = gauss_pi_method() #computes pi

    getcontext().prec = decimals #this block of code rounds pi to the number of decimal places asked for
    PiEst = +PiEst

    end_time = time.time()
    #next line prints the results
    print("Pi to " + str(decimals-1) + " decimal places is: " + str(PiEst))
    
    print("The algorithm ran in %s seconds" % (time.time() - start_time))
