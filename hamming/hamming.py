from math import ceil, log


def get_n(message):
    """
    Get the total number of bits corresponding to a message once encoded with
    a Hamming code.

    Arguments:
        - message (str): the binary message

    Returns:
        The total number of bits
    """
    return 2**(ceil(log(len(message))/log(2)) + 1) - 1


def get_m(message):
    """
    Get the number of parity bits needed for a message in order to be encoded
    with a Hamming code.

    Arguments:
        - message (str): the binary message

    Returns:
        The number of parity bits
    """
    return ceil(log(len(message))/log(2)) + 1
