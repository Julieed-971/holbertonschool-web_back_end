#!/usr/bin/env python3
"""Module that returns the log message obfuscated"""
import logging
import re
from typing import List
PII_FIELDS = ('name', 'email', 'ssn', 'password', 'phone')


def filter_datum(fields: List[str], redaction: str,
                 message: str, separator: str) -> str:
    """Function that returns the log message obfuscated"""
    for field in fields:
        message = re.sub((field + "=.*?" + separator),
                         (field + "=" + redaction + separator), message)
    return message


def get_logger() -> logging.Logger:
    """function that takes no arguments
    user_data = logging.getLogger(propagate=False)
    and returns a logging.Logger object."""
    user_data.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(RedactingFormatter)

    return user_data


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """filter values in incoming log records using filter_datum"""
        message = filter_datum(self.fields, self.REDACTION,
                               record.msg, self.SEPARATOR)
        record.msg = message
        return super().format(record)
