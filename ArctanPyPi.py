from fractions import Fraction #Imports fraction function to keep calculation as a fraction untill the end

def arctanpi(iterations): #defins a function for defining pi using the formula we derived

    result = Fraction(4) #result is a variable used to store our current value of pi as a fraction until it's needed as a decimal
    sign = -1 #sign keeps track of whether to add or subtract the fraction
    denominator = 3 #

    for i in range(0, iterations):
        result = result + (sign*Fraction(4, denominator))
        sign = 0 - sign
        denominator += 2

    return result

while 1:
    #Ask's the user how many iterations they want the algorithm to run for and saves the answer as an intiger
    iterations = int(input("Enter how many cycles you want the algorithm to run for: "))
    PiEst = arctanpi(iterations) #computes pi with as many iterations as you asked for
    PiDecimal = str(float(PiEst)) #gives you a decimal of the fraction the function computed.
    #next line prints the results
    print("After " + str(iterations) + "iterations the algorithm aproximated pi as" + str(PiEst.numerator) + "/" + str(PiEst.denominator) + " as a fraction or as a decimal: " + PiDecimal + " .")
    
