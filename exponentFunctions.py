def raise_to_power(base_num, pow_num):
    return base_num ** pow_num; # "**" is "to the power of


print(raise_to_power(2, 4));


# we can also do this using a for loop
def raise_to_power_for_loop(base_num, pow_num):
    result = 1;
    for power in range(pow_num):
        result *= base_num;
        # note that we will not use "power", the iterator object, at all. simply multiplying until we reach pow_num
    return result;


print(raise_to_power_for_loop(100, 4));

