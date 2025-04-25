#!/usr/bin/env python3
"""BasicCache module"""

from collections import defaultdict
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """FIFOCache is a caching system that inherits from BaseCaching.
    It implements a First-In-First-Out (FIFO) caching mechanism."""

    def __init__(self):
        """Initialize the cache and an order list to track insertion order."""
        super().__init__()
        self.order = []
        self.count = defaultdict(int)

    def put(self, key, item):
        """Store an item in the cache and remove the first
        one if number of elements in dict exceed the MAX"""
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.count[key] += 1
            self.order.append(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                min_val = min(self.count.values())
                results = [key for key, value
                           in self.count.items() if value == min_val]
                if len(results) > 1:
                    lru_key = self.order.pop(0)
                    del self.cache_data[lru_key]
                    print(f"DISCARD: {lru_key}")
                else:
                    del self.cache_data[results[0]]
                    print(f"DISCARD: {results[0]}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
