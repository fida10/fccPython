some_dictionary = {
    "Month" : "January",
    "Date" : 23,
    "Year" : 2010,
    "Male" : False,
    17 : "Age",
    True : "Yes"
}

# initialized with curly braces
# left side is key, then ":", then right side is value
# KEYS MUST BE UNIQUE
# similar in format to a json
# note that keys and values can basically be of any type, no need to define explicitly

print(some_dictionary["Month"]);
# key goes in the "[]", and the value for that key is returned
print(some_dictionary.get("18", "Not a valid value"));
# same as "[]", gets value for this key, with the added benefit of if key is not found, will return the second value specified ("Not a valid value", in this case)
