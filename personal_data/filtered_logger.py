#!/usr/bin/env python3
"""Module that returns the log message obfuscated"""
import logging
import mysql.connector
import re
import os
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
    and returns a logging.Logger object."""
    user_data = logging.getLogger()
    user_data.propagate = False
    user_data.setLevel(logging.INFO)

    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)
    ch.setFormatter(RedactingFormatter(list(PII_FIELDS)))
    user_data.handlers = []  # Remove any existing handlers
    user_data.addHandler(ch)

    return user_data


def get_db() -> mysql.connector.connection.MySQLConnection:
    """returns a connector to the database"""
    username = os.getenv('PERSONAL_DATA_DB_USERNAME')
    psswrd = os.getenv('PERSONAL_DATA_DB_PASSWORD')
    h = os.getenv('PERSONAL_DATA_DB_HOST')
    db = os.getenv('PERSONAL_DATA_DB_NAME')

    cnx = mysql.connector.connect(user=username,
                                  password=psswrd,
                                  host=h,
                                  database=db
                                  )
    return cnx


def main():
    """ function that takes no arguments and returns nothing"""
    db = get_db()
    cursor = db.cursor()
    cursor.execute("SELECT * FROM users")
    fields = ["name", "email", "phone", "ssn", "password"]
    logger = get_logger()
    for row in cursor:
        message = ("name=" + row[0] + "; email=" + row[1]
                   + "; phone=" + row[2] + "; ssn=" + row[3] +
                   "; password=" + row[4] + "; ip=" + row[5]
                   + "; last_login=" + row[6].strftime("%Y-%m-%d %H:%M:%S")
                   + "; user_agent="
                   + row[7] + ";"
                   )
        logger.info(message)


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


main()
