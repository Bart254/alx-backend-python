#!/usr/bin/env python3
""" Async generator module
"""
import random
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    """ async_generator function randomly generates a number between 0-10
    """
    for n in range(10):
        await asyncio.sleep(1)
        number = random.uniform(0, 10)
        yield number
