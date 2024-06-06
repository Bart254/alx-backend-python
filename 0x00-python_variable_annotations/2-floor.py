#!/usr/bin/env python3
""" Performs floor math operation

Functions:
    floor: returns the floor of a float
"""


def floor(n: float) -> int:
    """ Returns the floor of float arg

    Args:
        n (float): argument to perform floor operation on

    Returns:
        int: the result of floor operation on the argument
    """
    import math
    return math.floor(n)
