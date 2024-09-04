#!/usr/bin/env python3
"""Comprises class FIFOCache """

from base_caching import BaseCaching

class FIFOCache(BaseCaching):
    """  inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        if key is None or item is None:
            return
        cache_data = self.cache_data[key] = item
        max_items = super().MAX_ITEMS
        if len(self.cache_data) > max_items:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
