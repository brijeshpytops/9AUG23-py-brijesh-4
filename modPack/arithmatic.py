def sum(*args):
    """
    This function return sum of given value
    """
    total = 0
    for i in args:
        total += i
    return total


def mul(*args):
    """
    This function return sum of given value
    """
    total = 1
    for i in args:
        total *= i
    return total

def length(itrable_var):
    """
    This function return length of a itrable_var
    """
    count = 0 
    for i in itrable_var:
        count += 1
    return count