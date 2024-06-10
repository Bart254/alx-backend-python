#!/usr/bin/env python3
""" Asyncio task module """
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """ function task_wait_random creates async task

    Args:
        max_delay (int): maximum delay time

    Return:
        asyncio.Task: an async task
    """
    return asyncio.create_task(wait_random(max_delay))
