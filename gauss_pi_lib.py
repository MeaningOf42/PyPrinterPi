from decimal import *

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

