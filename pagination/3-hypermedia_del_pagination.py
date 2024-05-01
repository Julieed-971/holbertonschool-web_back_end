#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import Dict, List


class Server:
    """
    Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

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

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing
        pagination information for the current page
        """
        # retrieve the indexed dataset
        indexed_dataset = self.indexed_dataset()

        # calculate indexed dataset length
        dataset_len = len(indexed_dataset)

        # checks if index is within range of indexed dataset
        assert 0 <= index < dataset_len
        assert page_size > 0

        # calculate next index
        next_index = index + page_size

        # get the data from dataset in range of the page_size
        data = []
        for i in range(index, next_index):
            try:
                data.append(indexed_dataset[i])
            except KeyError:
                pass

        # returns a dictionnary with indexation information
        indexation_info = {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
        return indexation_info
