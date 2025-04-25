#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """FIFOCache is a caching system that inherits from BaseCaching.
    It implements a First-In-First-Out (FIFO) caching mechanism."""

    def __init__(self):
        """Initialize the cache and an order list to track insertion order."""
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Store an item in the cache and remove the first
        one if number of elements in dict exceed the MAX"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                last_key = self.order.pop(-2)
                del self.cache_data[last_key]
                print(f"DISCARD: {last_key}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
