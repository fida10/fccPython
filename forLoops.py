for letter in "Some Phrase":
    print(letter);

    # basically a for each loop, will iterate thru each char inside the string specified

someList = ["Hello", "I", "Am", "Sam"];

for indivElement in someList:
    print(indivElement);

    # loops through this list

# can also specify a range of values to loop through
for indivIndex in range(0, 2): # not including the second index (2)
    print(someList[indivIndex]);

# another way to loop through the entire list
for indivIndex in range(len(someList)): # len returns length of the list, will loop up to but not including that index
    print(someList[indivIndex]);
    print(indivIndex);
# the equivalend of a "for i" loop. indivIndex returns the current index loop is on, just like 'i'