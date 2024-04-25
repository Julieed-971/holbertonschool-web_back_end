#!/usr/bin/env python3
"""
Async coroutine calling async_generator and returning 10
random numbers collected
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """Async coroutine returning 10 random numbers"""
    return [random_number async for random_number in async_generator()]
