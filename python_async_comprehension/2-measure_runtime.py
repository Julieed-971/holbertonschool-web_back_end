#!/usr/bin/env python3
"""
Coroutine that measure runtime for executing
async_comprehension four times in parallel
"""

import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Coroutine that measure runtime for executing
    async_comprehension four times in parallel
    """
    start_time = time.time()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time
