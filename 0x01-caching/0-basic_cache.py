#!/usr/bin/env python3
""" comprise a BasicCache class"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ BasicCache that inherits from BaseCaching and is a caching system"""
    def __init__(self):
        super().__init__()

    def put(self, key, item):
        """
        assigns `item` to dictionary self.cache_data's key.
        Args:
            key (str) - key in a self.cache_data dictionary.
            item - value to be assigned to a key (can be any type)
        Return:
            modified dictionary
        """
        if key is None or item is None:
            return
        cache_data = self.cache_data[key] = item
        return cache_data

    def get(self, key):
        """
        retrieves a value  linked to `key` from self.cache_data dictionary.
        Args:
            key (str) - dictionary key
        Return:
            value associated with the key if the key exists, None otherwise.
        """
        return self.cache_data.get(key)
