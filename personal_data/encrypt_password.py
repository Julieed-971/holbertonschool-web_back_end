#!/usr/bin/env python3
"""Module that hashes and validate passwords"""
import bcrypt


def hash_password(password: str) -> bytes:
    """expects one string argument name password
    and returns a salted, hashed password, which is a byte string"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def is_valid(hashed_password: bytes, password: str) -> bool:
    """expects 2 arguments and returns a boolean"""
    bytes = password.encode('utf-8')
    return bcrypt.checkpw(bytes, hashed_password)
