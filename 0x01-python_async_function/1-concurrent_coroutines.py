#!/usr/bin/env python3
""" Concurrent coroutines module
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n function executes coroutine n number of times

    Args:
        n (int): number of times to execute coroutine

    Returns:
        list[float]: delay times per coroutine execution
    """
    # create tasks
    tasks = [wait_random() for i in range(n)]

    # await and capture tasks
    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
