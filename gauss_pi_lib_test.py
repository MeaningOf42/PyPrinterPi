import gauss_pi_lib
import time

while 1:
    #Ask's the user how many decimal places they want there answer to be given to
    decimals = int(input("Enter how many decimal places do you want pi to be given to: "))+1
    start_time = time.time()

    gauss_pi_lib.gauss_pi_method(decimals)
    
    
    end_time = time.time()
    #next line copies results from pi.txt
    f = open('pi.txt', 'r')
    pi = f.read()
    f.close()
    
    print("Pi to " + str(decimals-1) + " decimal places is: " + pi)
    
    print("The algorithm ran in %s seconds" % (time.time() - start_time))
