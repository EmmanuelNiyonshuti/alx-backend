#!/usr/bin/env python3
"""Comprises class FIFOCache """

from base_caching import BaseCaching
BasicCache = __import__("0-basic_cache").BasicCache

class FIFOCache(BaseCaching):
    """  Implements a FIFO caching system """

    def put(self, key, item):
        """
        overides `put` from BasicCache class,
        deletes the first inserted item from the dictionary `self.cache_data`
        and prints the removed item's key.
        Args:
            key (str)
            item -(can be of any type)
        Return:
            Void.
        """
        BasicCache.put(self, key, item)
        max_items = super().MAX_ITEMS
        if len(self.cache_data) > max_items:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD: {}".format(first_key))
    def get(self, key):
        """
        retrieves a value  linked to `key` from self.cache_data dictionary.
        Args:
            key (str) - dictionary key
        Return:
            value associated with the key if the key exists, None otherwise.
        """
        return BasicCache.get(self, key)
