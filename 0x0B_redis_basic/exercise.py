#!/usr/bin/env python3
"""Module to create a cache with Redis"""

import functools
import redis
import uuid
from typing import Union, Optional, Callable


def count_calls(count: Callable) -> Callable:
    """Decorator that counts calls to a method.
    
    Args:
        count (Callable): The method to be decorated.
        
    Returns:
        Callable: The wrapped method with call counting functionality.
    """
    key = count.__qualname__

    @functools.wraps(count)
    def wrapper(self, *args, **kwargs):
        self._redis.incr(key)

        return count(self, *args, **kwargs)
    return wrapper


class Cache:
    """Redis client class for caching data with automatic key generation."""
    
    def __init__(self) -> None:
        """Initialize the Redis client and flush the database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in Redis with a randomly generated key.
        
        Args:
            data (Union[str, bytes, int, float]): The data to store in Redis.
            
        Returns:
            str: The randomly generated key used to store the data.
        """
        rand_key = str(uuid.uuid4())
        self._redis.set(rand_key, data)
        return rand_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[
                str, bytes, int, float, None]:
        """Retrieve data from Redis and optionally convert it using a function.
        
        Args:
            key (str): The key to retrieve data for.
            fn (Optional[Callable]): Optional function to convert the data.
            
        Returns:
            Union[str, bytes, int, float, None]: The retrieved data, optionally 
            converted by fn, or None if key doesn't exist.
        """
        data = self._redis.get(key)

        if data is None:
            return None
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> Union[str, None]:
        """Retrieve data from Redis and convert it to a string.
        
        Args:
            key (str): The key to retrieve data for.
            
        Returns:
            Union[str, None]: The data as a UTF-8 decoded string, 
            or None if key doesn't exist.
        """
        return self.get(key, fn=lambda d: d.decode('utf-8'))

    def get_int(self, key: str) -> Union[int, None]:
        """Retrieve data from Redis and convert it to an integer.
        
        Args:
            key (str): The key to retrieve data for.
            
        Returns:
            Union[int, None]: The data as an integer, 
            or None if key doesn't exist.
        """
        return self.get(key, fn=int)
