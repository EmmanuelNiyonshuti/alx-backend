#!/usr/bin/env python3
""" MRU caching system """
from base_caching import BaseCaching
LRUCache = __import__("3-lru_cache").LRUCache


class MRUCache(BaseCaching):
    """ Implements Most Recent Used (LRU) caching algorithm """
    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add or update an item in the cache.
        - If the key already exists, update its value
          and move it to the end of the list.
        - If the key does not exist and the cache is full,
            remove the most recently used item (last item in the list).
        - Add the new item to the end of the list.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.key_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            mru_key = self.key_order.pop()
            del self.cache_data[mru_key]
            print(f"DISCARD: {mru_key}")
        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        - If the key exists, move it to the end of the list
            (mark it as most recently used) and return its value.
        - If the key does not exist, return None.
        """
        return LRUCache.get(self, key)
