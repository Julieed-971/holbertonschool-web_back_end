#!/usr/bin/env python3
import re

"""Module that returns the log message obfuscated"""


def filter_datum(fields, redaction, message, separator) -> str:
    """Function that returns the log message obfuscated"""
    for field in fields:
        pattern = rf"({field}=)(.*?){separator}"
        message = re.sub(pattern, rf"\1{redaction}{separator}", message)
    return message
