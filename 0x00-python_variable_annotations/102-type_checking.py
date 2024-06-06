#!/usr/bin/env python3
""" Codebase debugging
"""
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """ Returns list of modified items

    Args:
        lst (tuple): tuple to be iterated
        factor (int): integer to multiply tuple items with

    Returns:
        list: result of the multiplication of tuple items with lst
    """
    zoomed_in: List = [
        item for item in lst for i in range(factor)
    ]
    return zoomed_in


array: Tuple = tuple([12, 72, 91])
zoom_2x: List = zoom_array(array)
zoom_3x: List = zoom_array(array, 3)
