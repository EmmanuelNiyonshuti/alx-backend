#!/usr/bin/env python3
""" comprise a BasicCache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """assign to the dictionary self.cache_data
        the item value for the key `key` """
        if key is None or item is None:
            return
        cache_data = self.cache_data[key] = item
        return cache_data

    def get(self, key):
        """ return the value in self.cache_data linked to key """
        return self.cache_data.get(key)
