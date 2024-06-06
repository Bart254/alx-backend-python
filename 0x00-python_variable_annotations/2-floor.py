#!/usr/bin/python3
""" Performs floor mat operation
Modules:
    math: contains floor() method, which is used in operation

Functions:
    floor: returns the floor of a float
"""
import math


def floor(n: float) -> float:
    """ Returns the floor of float arg

    Args:
        n (float): argument to perform floor operation on

    Returns:
        float: the result of floor operation on the argument
    """
    return math.floor(n)
