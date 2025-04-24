#!/usr/bin/env python3
"""BasicCache module"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache is a caching system that inherits from BaseCaching.
    It provides basic functionality to store and retrieve items in a cache."""

    def put(self, key, item):
        """Store an item in the cache."""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve an item from the cache."""
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
