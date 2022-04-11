from math import *; # import statement, imports everything from math module

regInt = 2; # regular integer
floatInt = 2.103; # float
negInt = -3; # negative number

# basic operators
print(regInt + negInt);
print(regInt - negInt);

# +, -, /, *, % all work

result = regInt + negInt; # store result in a var


# further mathematical functions
print(abs(negInt)); # absolute value
print(pow(3, 2)); # 3 to the power 2
print(max(2, 5)); # prints out the higher number from the two specified. min does the opposite
print(round(3.2)) # rounds the number to the nearest whole number


# below depends on math import
print(floor(3.6)); # rounds the number to the nearest whole, downwards (i.e. this would return 3)
print(ceil(3.2)); # same as above, but upwards (i.e. this would return 4)
print(sqrt(36)); # returns square root

# see further documentation on math module for more.
