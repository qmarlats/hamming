from math import ceil, log

from utils import is_power_of_2
from vectors import get_canonical_basis_vectors


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


def get_k(message):
    """
    Get the number of data bits needed for a message in order to be encoded
    with a Hamming code.

    Arguments:
        - message (str): the binary message

    Returns:
        The number of data bits
    """
    return get_n(message) - get_m(message)


def get_g(message):
    """
    Get the generator matrix G which will allow to encode the message.

    Arguments:
        - message (str): the binary message

    Returns:
        The generator matrix
    """
    def set_parity_bits(vector, n):
        """
        Set the parity bits of a vector.

        Arguments:
            - vector (list): the vector for which parity bits must be set
            - n (int): the final length of the vector

        Returns:
            A vector with its parity bits
        """
        # Define parity bits indexes
        parity_bits_positions = [i for i in range(n) if is_power_of_2(i + 1)]

        # Fix vector length
        [vector.insert(i, 0) for i in range(n) if is_power_of_2(i + 1)]

        # Calculate parity bits
        for position in parity_bits_positions:
            for i, element in enumerate(vector):
                if (position + 1) & (i + 1) > 0 and element != 0:
                    vector[position] = 1

        return vector

    # Get n and k
    n = get_n(message)
    k = get_k(message)

    # Get canonical basis vectors
    vectors = get_canonical_basis_vectors(k)

    # Insert parity bits
    for vector in vectors:
        set_parity_bits(vector, n)

    # Define the generator matrix
    matrix = [
        [0 for j in range(len(vectors))]
        for i in range(len(vectors[0]))
    ]
    for i, vector in enumerate(vectors):
        for j, element in enumerate(vector):
            matrix[j][i] = element

    return matrix
