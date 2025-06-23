#!/usr/bin/env python3
"""Auth module"""
from flask import request
from typing import TypeVar, List
from models.base import Base


class Auth(Base):
    """Auth class"""

    def do_not_require_auth(self, path: str,
                            excluded_paths: List[str]) -> bool:
        """Define which routes don't need authentication"""
        if path is None or excluded_paths is None or not excluded_paths:
            return True
        if not path.endswith('/'):
            path += "/"
        excluded_paths = [p if p.endswith('/') else p + '/'
                          for p in excluded_paths]
        if path not in excluded_paths:
            return True
        return False

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        if request is None or request.headers.get("Authorization") is None:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """Returns None"""
        return None
