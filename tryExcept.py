try: # try block, notice format same as methods and if statements, colon and below is indent
    number = int(input("Enter a number: "));
    print(number);
except ZeroDivisionError as err: # exception error type specified here; in this case this except block is triggered if we divide by zero
    # "err" is basically the error message itself. We can print it as part of the except block
    print("Zero division!");
    print(f"Error message: {err}") # note that "err" is not a string so substitution/f-string must be used here
except ValueError as err: # same here but this time we use ValueError type
    print(f"Invalid input!");
    print(f"Error message: {err}")

# in this way, we can distinguish between exceptions

