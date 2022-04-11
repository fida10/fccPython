# take two numbers from user
# take operator from user
# execute operation that way


def calculator(num_one, num_two, operator):
    if(operator == "+"):
        return num_one + num_two;
    elif(operator == "-"):
        return num_one - num_two;
    elif(operator == "*"):
        return num_one * num_two;
    elif(operator == "/"):
        return num_one / num_two;
    elif(operator == "%"):
        return num_one % num_two;
    else:
        return "Invalid entry!";


num_one = float(input("Welcome to calculator better! Input your first number: "));
num_two = float(input("Input your second number: "));
# above are directly cast to floats from strings to make operations feasible (reason for having "float()")
operator = input("Now, input the operator you wish to execute upon these two numbers: ");

print(f"Your result: {calculator(num_one, num_two, operator)}");