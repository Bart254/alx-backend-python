#!/usr/bin/env python3
""" Sum module

Module:
    typing: variable annotation module

Functions:
    sum_mixed_list: returns sum of numbers in a list mixed with int and float
"""
from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """ Returns sum of numbers in passed list

    Args:
        mxd_list (list): list containing int and float

    Returns:
        float: sum of the numbers in the list
    """
    return sum(mxd_list)
