#!/usr/bin/env python3
""" async comprehension module
"""
import asyncio
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """ function async_comprehension loops through an async generator and
    returns 1- random numbers"""
    results = []
    async for n in async_generator():
        results.append(n)

    return results
