#!/usr/bin/env python3
"""
Returns the range of indexes according
to certain pagination parameters
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns the range of indexes according
    to certain pagination parameters
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
