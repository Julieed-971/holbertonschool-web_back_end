#!/usr/bin/env python3
"""
Type-annotated sum_mixed_list function taking a mxd_list list
of integers and floats and returning their sum as float
"""

import typing


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """Return the float type sum of a list of mixed type"""
    return float(sum(mxd_lst))
