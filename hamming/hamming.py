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
