is_a_degenerate = False;
# boolean value

is_mentally_challenged = True;

if is_a_degenerate:
    print("Go to rehab");
else:
    print("Good to go");

# basic if else statement, indents required in the place of curly braces

if is_a_degenerate and is_mentally_challenged:
    print("Seek help");

# an if statement with 2 booleans. "and" and "or" work just fine here, just like java

if is_a_degenerate:
    print("Seek help");
elif is_mentally_challenged:
    print("Really seek help");

# elif is the equivalent of else if


if not (is_a_degenerate):
    print("Good to go!!!");


# "not" works the same way as a "!", basically the opposite of the boolean within


def max_num_two_nums(num_one, num_two):
    if num_one <= num_two:
        # makes use of comparison operator. possible to use "<", ">", "<=", ">=", "!="
        return num_two;
    else:
        return num_one;


def max_num(num_one, num_two, num_three):
    first_max = max_num_two_nums(num_one, num_two);
    return max_num_two_nums(first_max, num_three)


print(max_num(32, 32, 17))

print(max_num('c', 'd', 'f'))
# auto converts chars to ascii values and compares them that way

print(max_num("Zello", "Zf", "Youyyyyyyyy"));