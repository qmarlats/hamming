def is_power_of_2(number):
    """
    Determine if a number is a power of 2 or not.

    Arguments:
        - number (int): the number to check

    Returns:
        A boolean, True if the number is a power of 2, False otherwise
    """
    return (number & (number - 1) == 0 and number > 0)
