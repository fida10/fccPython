import os
import os as OpSystem

friendsOne = open(f"{OpSystem.getcwd()}/friends.txt", "a"); # will append to the existing file
# note: using 'w' will automatically result in the old file getting erased!

friendsOne.write("\nRubin - SS");
friendsOne.write("\nMeh - Business");
# \n is a special character for starting a new line

# above will append two new lines to the file

friendsOne.close();

friendsTwo = open("../readingToFile/friends.txt", "w"); # as stated above, will delete the entire file and make it writeable

friendsTwo.write("\n Hola")
friendsTwo.close();

friendsThree = open(f"{OpSystem.getcwd()}/dasgafsdafdbadgb.txt", "w"); # because this file does not exist, this will actually CREATE a new file called "friendsTwo.txt" and then open it.

friendsThree.write("\n Hola")
friendsThree.close();


with open(f"{OpSystem.getcwd()}/dasgafsdafdbadgb.txt", "w") as friendsFour:
    friendsFour.write("\n some new line test");
