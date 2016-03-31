from decimal import *
import time

def gauss_pi_method():
    return 4*(12*arctan(18) + 8*arctan(57) - 5*arctan(239))

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

while 1:
    #Ask's the user how many decimal places they want there answer to be given to
    decimals = int(input("Enter how many decimal places do you want the answer to be given to: "))+1
    start_time = time.time()
    getcontext().prec = decimals+5 #sets precision to 4 more decimal places than asked for.
    
    PiEst = gauss_pi_method() #computes pi

    getcontext().prec = decimals #this block of code rounds pi to the number of decimal places asked for
    PiEst = +PiEst

    end_time = time.time()
    #next line prints the results
    print("Pi to " + str(decimals-1) + " decimal places is: " + str(PiEst))
    
    print("The algorithm ran in %s seconds" % (time.time() - start_time))
