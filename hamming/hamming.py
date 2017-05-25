from math import ceil, log

import numpy as np

from utils import is_power_of_2
from vectors import get_canonical_basis_vectors, to_vector


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


def get_h(message):
    """
    Get the parity-check matrix H which will allow to check the validity of the
    message and eventually find the error position.

    Arguments:
        - message (str): the binary message

    Returns:
        The parity-check matrix
    """
    # Get n
    n = len(message)

    # Get length necessary to represent n in binary
    length = n.bit_length()

    # Get binary numbers from 1 to n
    numbers = ['{0:0{1}b}'.format(i + 1, length) for i in range(n)]

    # Define the parity-check matrix
    matrix = []
    for i in range(length):
        matrix.append([])
        for number in numbers:
            matrix[i].append(int(number[i]))

    return matrix


def encode(message):
    """
    Encode a binary message with Hamming code.

    Arguments:
        - message (str): the binary message

    Returns:
        The encoded message
    """
    # Get G and the message as a vector
    g = get_g(message)
    message = to_vector(message)

    # Get the matrix product of G and the message
    matrix = np.dot(g, message)

    # Convert the result to a list of binary elements
    matrix = [int(bin(element)[-1:]) for element in matrix]

    return matrix


def decode(message):
    """
    Decode a binary message with Hamming code.

    Arguments:
        - message (str): the binary message

    Returns:
        The decoded message
    """
    # Get H
    h = get_h(message)

    # Get the matrix product of H and the message
    matrix = np.dot(h, message)

    # Convert the result to a list of binary elements
    matrix = [int(bin(element)[-1:]) for element in matrix]

    # Fix eventual errors
    if not all(element == 0 for element in matrix):
        position = int(''.join(str(element) for element in matrix), 2)
        message[position - 1] = int(bin(~message[position - 1])[-1:])

    return message
