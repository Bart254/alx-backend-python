#!/usr/bin/env python3
""" Module finds sum of numbers in a list

Modules:
    typing: variable annotation module

Functions:
    sum_list: returns the sum of numbers in a list parameter
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Returns sum of data in a list

    Args:
        input_list (list of float): list of float numbers

    Returns:
        float: the sum of al data in input_list
    """
    return sum(input_list)
