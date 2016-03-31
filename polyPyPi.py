from decimal import Decimal, getcontext


def pi_polygon(n):
    polygon_side_length_squared = Decimal(2)
    polygon_sides = 2
    for i in range(n):
        polygon_side_length_squared = 2 - 2 * (1 - (polygon_side_length_squared/4)).sqrt()
        polygon_sides = polygon_sides * 2
    return polygon_sides * polygon_side_length_squared.sqrt()

while 1:
    #Ask's the user how many iterations they want the algorithm to run for, and how many decimal places they want their answer to be give to.
    iterations = int(input("Enter how many cycles you want the algorithm to run for: ")) 
    places = int(input("Enter how many decimal places do you want the answer to be given to: "))

    getcontext().prec = places * 2 #sets precion to twice what's specified in order to avoid any rounding errors.

    if iterations > places: #if there are more iteratons than the number of decimals wanted this can lead to rounding errors, in this case it's best to do the calculations with twice the number of digits than iterations
        getcontext().prec = places * iterations * 2
    
    PiDecimal = pi_polygon(iterations) #calls the pi_polygon function to get the aproximation of pi
    
    getcontext().prec = places #sets the precision python works with to the number being asked
    PiDecimal = +PiDecimal #rounds value of pi to number of places python is using as defaul, which the previous line set to the number being asked for.
    print("After " + str(iterations) + " iterations, the algorith returned:" + str(PiDecimal)) #prints out the aproximation of pi
