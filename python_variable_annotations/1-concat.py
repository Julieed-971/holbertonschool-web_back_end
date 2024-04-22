#!/usr/bin/env python3
"""
Type-annotated concat function taking strings
as arguments and returning a concatenated string
"""
import typing


def concat(str1: str, str2: str) -> str:
    """Concatenate two strings"""
    return (str1 + str2)
