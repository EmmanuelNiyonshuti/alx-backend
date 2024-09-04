#!/usr/bin/env python3
"""Comprises class FIFOCache """

from base_caching import BaseCaching
BasicCache = __import__('0-basic_cache').BasicCache

class FIFOCache(BaseCaching):
    """  inherits from BaseCaching and is a caching system """
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        BasicCache.put(self, key, item)
        max_items = super().MAX_ITEMS
        if len(self.cache_data) > max_items:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        return BasicCache.get(self, key)
