peopleIKnow = ["SomeGuy", "LadyNextDoor", "SteveFromAccounting", "DudeFromLouisiana", 36, False];
someOtherList = ["dga", "fgafg", "dafads", "cdsadf", True, 4889, "dafads", "dafads", "dafads"];

peopleIKnow.extend(someOtherList);
# extend appends the "someOtherList" to the end of the "peopleIKnow" list
print(peopleIKnow);

peopleIKnow.append("Hola holy");
# appends "Hola holy" to the end of the peopleIKnow list
print(peopleIKnow);

peopleIKnow.insert(1, "Weeeeeee");
# inserts "Weeeee" at the index specified, and shifts everything to the right after the index
print(peopleIKnow);

peopleIKnow.remove("SteveFromAccounting");
# removes the specified value from the list
print(peopleIKnow);

peopleIKnow.pop();
# removes the very last element of this list
print(peopleIKnow);

print(peopleIKnow.index("dafads"));
# returns the index of the specified value within the list

print(peopleIKnow.count("dafads"));
# returns the number of times the specified value appears in the list

peopleIKnow.reverse();
# reverses the order of the list
print(peopleIKnow);

peopleIKnowTwo = peopleIKnow.copy();
# copies one list onto another reference
print(peopleIKnow);

peopleIKnow.sort();
# sorts the list in alphabetical order, though this only works if the list has all of the same data type (i.e. ALL string or ALL int's)
print(peopleIKnow);

peopleIKnow.clear();
# deletes EVERYTHING within the list
print(peopleIKnow);



#
#
#
#
# print(peopleIKnow[2]);
# # this will return the element at index 2 (slot 3) in the list
#
# print(peopleIKnow[-2]);
# # inputting a negative index will result in getting the element from the back of the list
# # in this example, we will get the second element from the back of the list, in this case, 36
# # in negatives, we do not start from 0.
#
# print(peopleIKnow[1:]);
# # gets part of the list. In this case, will return all elements after index 1, including index 1
#
# print(peopleIKnow[1:5]);
# # in this case, will return elements from index 1 to 5, including index 1 but not index 5
#
# print(peopleIKnow[:5]);
# # you get the idea. not including index 5, but all before it.
#
# peopleIKnow[3] = "DudeFromKentucky";
# # this updates the value at index 3 to the new value specified above.
# print(peopleIKnow[3]);
#
