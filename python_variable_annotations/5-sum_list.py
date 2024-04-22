#!/usr/bin/env python3
"""
Type-annotated function sum_list taking an input_list
of floats as arguments and returning their float sum
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """Return the sum of a list of floats"""
    return float(sum(input_list))
