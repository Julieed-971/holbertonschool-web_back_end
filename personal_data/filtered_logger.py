#!/usr/bin/env python3
import re
from typing import List

"""Module that returns the log message obfuscated"""


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function that returns the log message obfuscated"""
    for field in fields:
        message = re.sub((field + "=.*?" + separator),
                         (field + "=" + redaction + separator), message)
    return message
