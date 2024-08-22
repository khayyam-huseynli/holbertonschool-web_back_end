#!/usr/bin/env python3
''' Description: Implement a get_hyper method that takes the same arguments
                 (and defaults) as get_page and returns a dictionary containing
                 the following key-value pairs:

        - page_size: the length of the returned dataset page
        - page: the current page number
        - data: the dataset page (equivalent to return from previous task)
        - next_page: number of the next page, None if no next page
        - prev_page: number of the previous page, None if no previous page
        -total_pages: the total number of pages in the dataset as an integer
    Make sure to reuse get_page in your implementation.
    You can use the math module if necessary.
'''

import csv
import math
from typing import List, Tuple, Dict, Any


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """Return a tuple containing the start and end indexes for
    a given page and page_size."""
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset"""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip header

        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict[str, Any]:
        """Return the appropriate page of the dataset."""
        assert isinstance(page, int) and page > 0, \
            f"page must be an integer greater than 0, got {page}"
        assert isinstance(page_size, int) and page_size > 0, \
            f"page_size must be an integer greater than 0, got {page_size}"

        start_index, end_index = index_range(page, page_size)
        dataset = self.dataset()

        prev_page = page - 1
        next_page = page + 1
        total_pages = math.ceil(len(dataset) / page_size)

        if start_index >= len(dataset):
            dataset = []
            page_size = 0
            next_page = 'None'

        if prev_page < 1:
            prev_page = 'None'

        return {
            'page_size': page_size,
            'page': page,
            'data': dataset[start_index:end_index],
            'next_page': next_page,
            'prev_page': prev_page,
            'total_pages': total_pages
        }
