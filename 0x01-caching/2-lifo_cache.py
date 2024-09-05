#!/usr/bin/env python3
""" comprises LIFOCache class implementation """
from base_caching import BaseCaching
BasicCache = __import__("0-basic_cache").BasicCache


class LIFOCache(BaseCaching):
    """ Implements lifo caching system """

    def __init__(self):
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        implements LIFO. when the cache reaches the required
        capacity(max_items) discards the most recently
        added or updated item in the cache.
        Args:
            key (str)
            item (can be of any type)
        Return:
            Void.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.stack.remove(key)

        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.stack.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """
        retrieves a value  linked to `key` from self.cache_data dictionary.
        Args:
            key (str) - dictionary key
        Return:
            value associated with the key if the key exists, None otherwise.
        """
        return BasicCache.get(self, key)
