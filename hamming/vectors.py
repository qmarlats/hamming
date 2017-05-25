def get_canonical_basis_vectors(dimension):
    """
    Get the canonical basis vectors for a vector space of a certain dimension.

    Arguments:
        - dimension (int): the dimension of the vector space

    Returns:
        A list containing the canonical basis vectors
    """
    vectors = [
        [1 if j == i else 0 for j in range(dimension)]  # Element in vector
        for i in range(dimension)  # Vector
    ]

    return vectors


def to_vector(message):
    """
    Convert a binary message into a vector.

    Arguments:
        - message (str): the binary message

    Returns:
        The message as a vector
    """
    return [int(element) for element in message]
