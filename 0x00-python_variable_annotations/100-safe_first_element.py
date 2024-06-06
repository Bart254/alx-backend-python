#!/usr/bin/env python3
""" Sequence Any and Optional annotations
"""
from typing import Sequence, Any, Optional


# The types of the elements of the input are not known
def safe_first_element(lst: Sequence[Any]) -> Optional[Any]:
    """ Returns the first element of a sequence

    Args:
        lst (Sequence): any datatype that can be indexed

    Returns:
        [Any, None]: first element of the index if any, otherwise none
    """
    if lst:
        return lst[0]
    else:
        return None
