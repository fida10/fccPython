# import readingToFile.readingToFile
from readingToFile import modulesImportEx # more precise import statement, can also import * from readingToFile, imports everything underneath that directory
# import readingToFile.a.somadsf as a # can also import in this way, "." is basically file separator, just like python. To call the contents of this import, we call it "a"
#
modulesImportEx.someFunctions(); # so this will only call the someFunctions method, and will not run the code within other methods inside of the modulesImportEx.py file
# a.someTest(); # using "a"

