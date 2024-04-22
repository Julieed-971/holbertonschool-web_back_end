#!/usr/bin/env python3
"""
Type-annotated make_multiplier function taking a float multiplier
as argument and returning a function multiplying a float by multiplier
"""

import typing


def make_multiplier(multiplier: float) -> typing.Callable[[float], float]:
    """Return a function that multiplies a float by multiplier"""
    def multiply(num: float) -> float:
        return num * multiplier
    return multiply
