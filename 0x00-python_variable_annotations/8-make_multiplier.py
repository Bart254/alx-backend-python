#!/usr/bin/env python3
""" Closure functions

Module:
    typing: variable annotation module

Functions:
    make_multiplier: returns a multiplication function
    multiply: function returned by make_multiplier. It finds the product
    of argument passed to it and previous arg passed to make_multiplier
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ Returns a function

    Args:
        multiplier (float): first operand for multiplication

    Returns:
        function: returns product of multiplier and arg passed to it
    """
    def multiply(value: float) -> float:
        """ Returns product of multiplier and arg passed to it

            Args:
                value (float): arg to multiply with multiplier

            Returns:
                float: product of value and multiplier
        """
        return value * multiplier
    return multiply
