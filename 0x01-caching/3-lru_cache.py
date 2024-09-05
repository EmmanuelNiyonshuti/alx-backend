#!/usr/bin/env python3
""" LRU caching system """
from base_caching import BaseCaching

class LRUCache(BaseCaching):
    """ Implements Least Recent Used (LRU) caching algorithm """
    def __init__(self):
        super().__init__()
        self.key_order = []

    def put(self, key, item):
        """
        Add or update an item in the cache.
        
        - If the key already exists, update its value
          and move it to the end of the list.
        - If the key does not exist and the cache is full,
            remove the least recently used item (first item in the list).
        - Add the new item to the end of the list.
        """
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.key_order.remove(key)
        elif len(self.cache_data) >= self.MAX_ITEMS:
            lru_key = self.key_order.pop(0)
            del self.cache_data[lru_key]
            print(f"DICARD: {lru_key}")
        self.cache_data[key] = item
        self.key_order.append(key)

    def get(self, key):
        """
        Retrieve an item from the cache.
        
        - If the key exists, move it to the end of the list
            (mark it as most recently used) and return its value.
        - If the key does not exist, return None.
        """
        value = self.cache_data.get(key)
        if value is not None:
            self.key_order.remove(key)
            self.key_order.append(key)
            return value
        return None
