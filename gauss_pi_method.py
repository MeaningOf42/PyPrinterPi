from decimal import *

def gauss_pi_method():
    return 4*(12*arctan(18) + 8*arctan(57) - 5*arctan(239))

def arctan(x): #defins a function for defining pi using the formula we derived
    
    acuracy = Decimal(Decimal(1)/Decimal(10**(getcontext().prec-3)))
    result = Decimal(Decimal(1)/Decimal(x)) #result is a variable used to store our current value of pi as a decimal, 1 and x are turned into  decimals to avoid rounding errors
    sign = -1 #sign keeps track of whether to add or subtract the fraction
    denominatorval = 3 #
    fract = 0 #fraction keeps the value of the fraction we want to add or subtract to the result, it is later used to see if function can stop.
    
    while True:
        fract = Decimal(Decimal(1)/(denominatorval*(Decimal(x)**denominatorval)))
        result += sign*(fract)
        if fract<acuracy:
            break
        sign *= -1
        denominatorval += 2

    return result

while 1:
    #Ask's the user how many decimal places they want there answer to be given to
    decimals = int(input("Enter how many decimal places do you want the answer to be given to: "))+1

    getcontext().prec = decimals+4 #sets precision to 4 more decimal places than asked for.
    
    PiEst = gauss_pi_method() #computes pi

    getcontext().prec = decimals #this block of code rounds pi to the number of decimal places asked for
    PiEst = +PiEst
    
    #next line prints the results
    print("Pi to " + str(decimals-1) + " decimal places is: " + str(PiEst))
    
