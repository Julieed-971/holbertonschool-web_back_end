#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import TypeVar, List
from models.base import Base


class Auth(Base):
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Define which routes don't need authentication"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += "/"
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return None
