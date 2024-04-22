#!/usr/bin/env python3
"""
A script that defines a function to get the length
of each element in an iterable of sequences.
"""
import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    """
    Return a list of tuples, where each tuple contains
    a sequence and its length.
    """
    return tuple([(i, len(i)) for i in lst])
