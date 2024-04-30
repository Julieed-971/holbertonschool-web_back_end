#!/usr/bin/env python3
"""
Returns the range of indexes according
to certain pagination parameters
"""

import csv
import math
from typing import List, Tuple, Dict


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

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionnary containing various
        information about dataset pagination
        """
        current_page = self.get_page(page, page_size)
        len_page = len(current_page)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)
        prev_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None
        return {
            "page_size": len_page,
            "page": page,
            "data": current_page,
            "next-page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages,
        }
