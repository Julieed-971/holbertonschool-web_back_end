#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import TypeVar, List
from models.base import Base


class Auth(Base):
    """Auth class"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """Determine if require authentication"""
        return False

    def authorization_header(self, request=None) -> str:
        """"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """"""
        return None
