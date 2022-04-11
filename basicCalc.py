numOne = input("Input number one: ");
numTwo = input("Input number two: ");

result = float(numOne) + float(numTwo);
# python by default takes input as strings. We must convert them into floats, which is what float() does
# can also do int() but this would mean the calculator does not accept decimals.

print(result);
