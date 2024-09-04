#!/usr/bin/env python3
""" comprises LIFOCache class implementation """
from base_caching import BaseCaching
BasicCache = __import__("0-basic_cache").BasicCache


class LIFOCache(BaseCaching):
    """ Implements lifo caching system """

    def put(self, key, item):
        """
        overides `put` from BasicCache class,
        deletes the last inserted item (or the recent inserted item)
        from the dictionary `self.cache_data` (implementing lifo)
        if the size of the dictionary is higher than
        the required maximum items and prints the removed item's key.
        Args:
            key (str)
            item (can be of any type)
        Return:
            Void.
        """
        BasicCache.put(key, item)
        max_items = super().MAX_ITEMS
        if len(self.cache_data) > max_items:
            last_item = self.cache_data.popitem()
            print(f"DISCARD: {last_item[0]}")

    def get(self, key):
        """
        retrieves a value  linked to `key` from self.cache_data dictionary.
        Args:
            key (str) - dictionary key
        Return:
            value associated with the key if the key exists, None otherwise.
        """
        return BasicCache.get(key)
