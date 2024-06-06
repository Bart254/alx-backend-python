#!/usr/bin/env python3
""" Tuple from string, int/float

Module:
    typing: variable annotation module

Functions:
    to_kv: returns a tuple from a string and int/float
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """ Returns a tuple containing str and int/float

    Args:
        k (str): string
        v (int/float): integer or float argument

    Returns:
        tuple: Tuple containing k and square of v
    """
    return k, float(v ** 2)
