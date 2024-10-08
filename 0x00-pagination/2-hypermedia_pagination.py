#!/usr/bin/env python3
"""Module for paginating a dataset of popular baby names. """
import csv
import math
from typing import List, Dict
index_range = __import__("0-simple_helper_function").index_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the cached dataset.

        Loads the dataset from the CSV file if not already loaded.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns a page of the dataset.

        Args:
            page (int): The page number (1-based).
            page_size (int): The number of items per page.

        Returns:
            List[List]: A list of rows for the specified page.
        """
        assert isinstance(page, int) and isinstance(page_size, int)
        assert page_size > 0 and page > 0
        page = index_range(page, page_size)
        data = self.dataset()
        return [data[i] for i in range(page[0], page[-1]) if i < len(data)]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[int, List]:
        """
        Returns a dictionary containing pagination information.

        Args:
            page (int): The current page number.
            page_size (int): The number of items per page.

        Returns:
            Dict: A dictionary with pagination details.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None
        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
            }
