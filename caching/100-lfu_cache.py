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
                self.cache_data[key] = item
                self.count[key] += 1
                self.order.remove(key)
                self.order.append(key)
            else:
                self.cache_data[key] = item
                self.count[key] = 1
                self.order.append(key)

                if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                    min_val = min(self.count.values())
                    results = [key for key
                               in self.order if self.count[key] == min_val]
                    lfu_key = results[0]
                    self.order.remove(lfu_key)
                    del self.cache_data[lfu_key]
                    del self.count[lfu_key]
                    print(f"DISCARD: {lfu_key}")

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            self.count[key] += 1
            self.order.remove(key)
            self.order.append(key)
            return self.cache_data[key]
        return None
