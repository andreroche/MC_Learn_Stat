# the number we will perform the collatz operation on.
#n = 20
# or use this

n = int(input("Enter a Positive Integer::"))

# Keep looping until we reach 1. 
# Note: this assumes the collatz conjecture is true.
while n != 1:
    print (n) # prints the current value of n
    if n % 2 == 0: # if n is even divide it by 2 
        n = n/2
    else:
        n = (3 * n) + 1 # if n is odd, multiply by 3 and add 1 



print (n) # finally , print the 1.
