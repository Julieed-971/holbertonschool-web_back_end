#!/usr/bin/env python3
"""
Coroutine that yield a random number between 0 and 10
"""

import asyncio
import random
from typing import List, AsyncGenerator


async def async_generator() -> AsyncGenerator[float, float]:
    """Coroutine that yield a random number between 0 and 10"""
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
