#!/usr/bin/env python3
"""Module for session authentication"""
from api.v1.auth.auth import Auth
from models.user import User
from typing import TypeVar
import base64
import uuid


class SessionAuth(Auth):
    """Session auth class that inherit from auth"""
    user_id_by_session_id = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or type(user_id) is not str:
            return None
        self.session_id = str(uuid.uuid4())
        self.user_id_by_session_id[self.session_id] = user_id
        return self.user_id_by_session_id
