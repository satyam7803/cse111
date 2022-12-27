import math
a=math.radians(90)
print(math.sin(a))
print(math.cos(a))
print(math.tan(a))

print(math.pow(2,4))            # power of 2 raise to power 4
print(math.sqrt(64))            # returns the square root of the value
print(math.fabs(-15))           # returns the absolute/positive value of a number
print(math.factorial(5))        # retuens the factorial of a number
print(math.fsum([1,2,3,4,5,6,7,8,9,10]))  # returns the sum of all integers in the lists, tuples or arrays
print(math.prod([1,2,3,4,5,6,7,8,9,10]))  # returns the product of all integers in the lists, tuples or arrays
print(math.log(10,2))               #returns natural log of 10 with base 2
print(math.gcd(48,54))              # greatest common divisor of a number
print(math.hypot(3,4))          # hypotenuse of triangle with sides 3,4
print(math.pi)
print(math.tau)
print(math.nan)
print(math.comb(4,2))       # to number of outcome to choose 2 things from 4 things

"""
example of math.comb
    1,2,3,4
        1. 1,2
        2. 1,3
        3. 1,4
        4. 2,3
        5. 2,4
        6. 3,4  
"""
print(math.dist([3,3], [4,4]))