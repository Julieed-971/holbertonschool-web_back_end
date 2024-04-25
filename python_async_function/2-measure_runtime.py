#!/usr/bin/env python3
"""Measure the approximate execution time of wait_n function"""

import asyncio
import time


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int) -> float:
    """Measure the approximate elapsed time during wait_n execution"""
    start_time = time.time()
    asyncio.run(wait_n(n, max_delay))
    finish_time = time.time()
    total_time = finish_time - start_time
    return (total_time / n)
