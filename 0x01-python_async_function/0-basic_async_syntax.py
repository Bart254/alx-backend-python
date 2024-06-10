#!/usr/bin/env python3
""" Async syntax module
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ Function wait_random waits for a random delay between 0 and max_delay

    Args:
        max_delay (int): maximum delay in seconds

    Returns:
        float: actual delay time in seconds
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
