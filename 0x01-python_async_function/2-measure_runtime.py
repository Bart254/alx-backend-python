#!/usr/bin/env python3
""" Module measures runtime of async functions
"""
import time
import asyncio
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    """ function measure_time measures the total execution
    time """
    start: float = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end: float = time.perf_counter()
    return (end - start) / n
