import os

friendsFile = open(f"{os.getcwd()}/readingToFile/friends.txt", "r")
# "open" opens the file specified in this relative path (indicated by "../"
# the information within is then stored inside of the "friendsFile" variable
# "r" means to read. There are several other options:
'''
r = read
w = write
a = append (append to the end of the file, cannot change)
r+ = read and write, master access
'''

print(friendsFile.readable()); # returns a boolean value to see if the file is readable by python

print(friendsFile.readline());
print(friendsFile.readline()); # for reading lines. This is an iterator; if readline has already been done once, doing it again will read the next line down.
# so in this case, this would print the first two lines

print(friendsFile.readlines()); # this returns an array. each line is an element in that array
# print(friendsFile.readlines()[0]); # same command as above but for a specific line in the text file, denoted by index

# note that "readLines" and "readLine" work in tandem; here, the first two "readLine"'s will push the reader to the 3rd line. Then, "readLines" from line 18 will read ALL the lines and force the reader to the bottom.
# Line 19 will throw an exception since there is nothing left to read!

friendsFile.close(); # a file should be closed once we are done with it (recommended)

friendsFileTwo = open(f"{os.getcwd()}/readingToFile/friends.txt");
for indivFriend in friendsFileTwo: # for loop to print out every line in the text file
    print(indivFriend);
friendsFileTwo.close();

def someMethod():
    print("green");
