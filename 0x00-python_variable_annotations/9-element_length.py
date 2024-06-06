#!/usr/bin/env python3
""" Iterables and Sequences

Module:
    typing: variable annotation module

Functions:
    element_length: Returns a list of tuples
"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """ Returns a list of tuples

    Args:
        element_length (iterable): an iterable object

    Returns:
        list: a list of tuples containing lst elements and their length
    """
    return [(i, len(i)) for i in lst]
