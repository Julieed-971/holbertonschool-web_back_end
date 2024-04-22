#!/usr/bin/env python3
"""Return an element and its length"""

import typing


def element_length(
        lst: typing.Iterable[typing.Sequence]
        ) -> typing.List[typing.Tuple[typing.Sequence, int]]:
    return [(i, len(i)) for i in lst]
