#!/usr/bin/env python3
"""Measures exceution runtime
"""
import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ Returns the runtime of executing async_comprehension
    """
    start = time.perf_counter()

    # run comprehension asynchronously
    await asyncio.gather(*(async_comprehension() for i in range(4)))

    end = time.perf_counter()
    return end - start
