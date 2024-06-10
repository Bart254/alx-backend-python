#!/usr/bin/env python3
""" Concurrent coroutines module
"""
import time
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """ task_wait_n function executes coroutine n number of times

    Args:
        n (int): number of times to execute coroutine

    Returns:
        list[float]: delay times per coroutine execution
    """
    # create tasks
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # await and capture tasks
    results = []
    for task in asyncio.as_completed(tasks):
        results.append(await task)

    return results
