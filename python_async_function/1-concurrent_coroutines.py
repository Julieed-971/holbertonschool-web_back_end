#!/usr/bin/env python3
"""
Async routine that spawn wait_random n times and returns
the list of all the delays as float values
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of multiples coroutines delays values"""
    coroutines = [wait_random(max_delay) for _ in range(n)]
    delays_list = await asyncio.gather(*coroutines)
    return sorted(delays_list)
