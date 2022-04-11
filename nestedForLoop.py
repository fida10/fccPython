twoDList = [
    [1, 3, 5],
    [3, 6, 8],
    [1, 2],
    [4, 6, 3, 12, 32]
]

# to print out the ALL the elements within the 2d array, use a nested for loop:

for indivList in twoDList:
    # indivList is each individual list inside of twoDList
    for indivElement in indivList:
        # indivElement is each individual element inside of indivList
        print(indivElement);
