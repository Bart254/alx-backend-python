#!/usr/bin/env python3
""" Generic annotations
"""
from typing import Mapping, Any, Optional, Union, TypeVar
T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any, default: Optional[T] = None)\
 -> Union[Any, T]:
    """ Returns dictionary key

    Args:
        dct: dictionary
        key (any type): key to look for in the dictionary
        default (T): default data that is returned if key is not found in dct

    Returns:
        any datatype: the value in dictionary, or, default
    """
    if key in dct:
        return dct[key]
    else:
        return default
