"""
This is the validator module as the pythonic way for mimicking "a class with static methods"
Since python treats number as a single type of number therefore we removed the other methods
"""


def get_string(prompt):
    val = input(prompt)
    return val.strip()


def get_int(prompt, min_val=0, at_least=False):
    val = input(prompt)
    if not val.isdigit():
        print("Invalid value, Try again!")
        return get_int(prompt)
    if min_val == 0:
        return int(val)
    else:
        if at_least:
            if int(val) <= min_val:
                return int(val)
            else:
                print("Number at least {0}".format(min_val))
                return get_int(prompt, min_val, False)
        else:
            if int(val) < min_val:
                return int(val)
            else:
                print("Number must be more than {0}".format(min_val))
                return get_int(prompt, min_val, True)