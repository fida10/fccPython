def someFunction():
    print("Hello how are you");


# in the place of curly braces, functions use ":"
# contents of a function are denoted by an indent. THIS IS MANDATORY

# function with params:
def someOtherFunction(name):
    print("Hellow how are you " + name)


# in order to use this function, we must call it. No need for a main method

someFunction();
someOtherFunction("Eshad");


def cube_a_function(integerToCube):
    return integerToCube * integerToCube * integerToCube;

# return values with the "return" keyword


print(cube_a_function(5));
# print out the returned value
