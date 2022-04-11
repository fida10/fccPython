# various functions we can do with strings

print("Hello \n there!"); # start new line at \n
print("Put a quote \" here!"); # will add a quotation mark to the string at \"

phrase = "This is a String variable!";
print(phrase);

print(phrase + " And now you can too!"); # concatenation at '+'

print(phrase.upper()); # turns all chars in string to upper case
print(phrase.lower()); # turns all chars in string to lower case

print(phrase.isupper()); # checks to see if the string is all upper case; returns boolean
# equiv method for lower case exists, islower()

print(phrase.upper().isupper()); # combination

print(len(phrase)); # return length of string

print(phrase[2]); # return char at a specified index (in this case, 3rd letter or 2nd index)

print(phrase.index('s')); # return index of the first char that matches what was specified
# can also specify a string here (or substring) and will return where that substring starts in the main string
# no matches will throw an error

print(phrase.replace("is", "dah")); # replaces all matches with what was specified

