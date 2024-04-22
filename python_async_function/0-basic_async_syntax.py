#!/usr/bin/env python3
"""
Asynchronous coroutine taking an integer argument that
waits for a random delay between 0 and max_delay and
eventually returns it
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Wait for a random delay between 0 and max_delay and return it"""
    actual_delay = random.uniform(0, max_delay)
    await asyncio.sleep(actual_delay)
    return actual_delay
