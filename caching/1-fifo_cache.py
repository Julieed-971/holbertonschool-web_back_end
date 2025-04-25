#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system that inherits from BaseCaching.
    It implements a First-In-First-Out (FIFO) caching mechanism."""

    def put(self, key, item):
        """Store an item in the cache and remove the first
        one if number of elements in dict exceed the MAX"""
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                del self.cache_data[first_key]
                print(f"DISCARD: {first_key}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
