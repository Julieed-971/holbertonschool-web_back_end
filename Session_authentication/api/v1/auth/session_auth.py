#!/usr/bin/env python3
"""Module for session authentication"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


class SessionAuth(Auth):
    """Session auth class that inherit from auth"""
