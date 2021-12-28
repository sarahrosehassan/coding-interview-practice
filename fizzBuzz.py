"""
Write a program that prints the numbers from 1 to n. 
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”.
For numbers which are multiples of both three and five print “FizzBuzz”.
"""

def fizzBuzz(n):
    for i in range(1,n+1):
        if (i % 5) == 0 and (i % 3) == 0:
            print('FizzBuzz')
        
        elif (i % 3) == 0 and (i % 5) != 0:
            print('Fizz')
            
        elif (i % 5) == 0 and (i % 3) !=0:
            print('Buzz')
                  
        elif (i % 5) != 0 and (i % 3) != 0:
            print(i)
            
# Alternate solution
def fizzBuzz2(n):
    for n in xrange(1, 101):
        print("Fizz"*(n % 3 == 0) + "Buzz"*(n % 5 == 0) or n)
