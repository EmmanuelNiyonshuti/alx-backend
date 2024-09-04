#!/usr/bin/env python3
"""Comprises class FIFOCache """

BasicCache = __import__('0-basic_cache').BasicCache

class FIFOCache(BasicCache):
    """  inherits from BaseCaching and is a caching system """
    def put(self, key, item):
        super().put(key, item)
        max_items = super().MAX_ITEMS
        if len(self.cache_data) > max_items:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print(f"DISCARD: {first_key}")

    def get(self, key):
        return super().get(key)
