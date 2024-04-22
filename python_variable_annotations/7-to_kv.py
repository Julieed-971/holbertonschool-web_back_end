#!/usr/bin/env python3
"""
Type-annotated to_kv function taking a string k and an int
or float v as arguments and return a tuple
"""

import typing


def to_kv(k: str, v: typing.Union[int, float]) -> typing.Tuple[str, float]:
    """Return a tuple of a string k and the square of a number"""
    kv_tuple = (k, v**2)
    return kv_tuple
