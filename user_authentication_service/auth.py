#!/usr/bin/env python3
"""Module to authenticate users"""
from db import DB
from user import Base, User
from sqlalchemy.orm.exc import NoResultFound
import bcrypt
import uuid


def _hash_password(password: str) -> bytes:
    """expects one string argument name password
    and returns a salted, hashed password, which is a byte string"""
    bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hash = bcrypt.hashpw(bytes, salt)
    return hash


def _generate_uuid() -> str:
    """return a string representation of a new UUID"""
    return str(uuid.uuid4())


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """Register a user if doesn't exist in the database"""
        db = self._db
        try:
            db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_password = _hash_password(password)
            new_user = self._db.add_user(email, hashed_password)
        return new_user

    def valid_login(self, email: str, password: str) -> bool:
        """Check if the password is valid"""
        bytes = password.encode('utf-8')
        try:
            user = self._db.find_user_by(email=email)
            user_psswrd = user.hashed_password
            result = bcrypt.checkpw(bytes, user_psswrd)
            return result
        except NoResultFound:
            return False
