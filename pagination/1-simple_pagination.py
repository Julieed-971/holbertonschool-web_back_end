#!/usr/bin/env python3
"""
Returns the range of indexes according
to certain pagination parameters
"""

import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the range of indexes according
    to certain pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Find the correct indexes to paginate dataset
        and return the appropriate page
        """
        # Verify that both arguments are integers greater than 0
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Use index_range to find the indexes to
        # paginate dataset and return appropriate page
        try:
            page_range = index_range(page, page_size)
            return self.dataset()[page_range[0]:page_range[1]]
        except AssertionError:
            Exception
