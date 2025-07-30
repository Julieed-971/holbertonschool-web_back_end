#!/usr/bin/env python3
"""Module to create a cache with Redis"""

import redis
import uuid


class Cache():
    """Redis client class"""
    def __init__(self) -> None:
        """Instantiate the redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: str | bytes | int | float) -> str:
        """
        Store data in Redis with a random key.
        
        Args:
            data: The data to store (str, bytes, int, or float)
            
        Returns:
            The generated key as a string
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key
