#!/usr/bin/env python3
import re


"""Module that returns the log message obfuscated"""


def filter_datum(fields: list,
                 redaction: str, message: str, separator: str) -> str:
    """fields: a list of strings representing all fields to obfuscate
    redaction: a string representing by what the field will be obfuscated
    message: a string representing the log line
    separator: a string representing by which character is separating
        all fields in the log line (message)"""

    for field in fields:
        pattern = rf"({field}=)(.*?){separator}"
        message = re.sub(pattern, rf"\1{redaction}{separator}", message)
    return message
