# Can use variables in python

characterName = "Vegeta";
characterAge = 25; # integer variable
isHuman = False; # boolean variable
# note that data type does not need to be explicitly stated

print("His name is " + characterName);
print("His age is " + str(characterAge));
print("Is he human? " + str(isHuman));
print(f"is he human {characterAge}"); # String formatting without converting to str
# Must convert data types that are not strings to strings when concatenating ('+')
# Else print statement will not work

