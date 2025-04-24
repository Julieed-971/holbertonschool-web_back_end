#!/usr/bin/env python3

from base_caching import BaseCaching

"""BasicCache module
"""


class BasicCache(BaseCaching):
    """
    BasicCache is a caching system that inherits from BaseCaching. It provides
    basic functionality to store and retrieve items in a cache.
    Methods:
        put(key, item):
            Adds an item to the cache with the specified key. If either the key
            or the item is None, the method does nothing.
        get(key):
            Retrieves an item from the cache using the specified key.
            If the key is None or does not exist in the cache,
            the method returns None.
    """

    def put(self, key, item):
        """
        Store an item in the cache.

        Args:
            key (str): The key under which the item will be stored.
            item (any): The item to store in the cache.

        Notes:
            If either `key` or `item` is None, the method does nothing.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Retrieve an item from the cache.

        Args:
            key (str): The key of the item to retrieve.

        Returns:
            The value associated with the key if it exists and is not None,
            otherwise None.
        """
        if key is not None and key in self.cache_data:
            return self.cache_data[key]
        return None
