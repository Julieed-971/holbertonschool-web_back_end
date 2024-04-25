#!/usr/bin/env python3
"""Measure the approximate execution time of wait_n function"""


import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of multiples coroutines delays values"""
    coroutines = [task_wait_random(max_delay) for _ in range(n)]
    delays_list = await asyncio.gather(*coroutines)
    return sorted(delays_list)
