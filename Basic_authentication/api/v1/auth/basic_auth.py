#!/usr/bin/env python3
"""Module for basic authentication"""
from api.v1.auth.auth import Auth
import base64


class BasicAuth(Auth):
    """Basic auth class that inherit from Auth"""

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """returns the Base64 part of the
        Authorization header for a Basic Authentication"""
        if authorization_header is None:
            return None
        if type(authorization_header) is not str:
            return None
        if not authorization_header.startswith('Basic '):
            return None
        return authorization_header[6:]

    def decode_base64_authorization_header(self,
                                           base64_authorization_header:
                                               str) -> str:
        """returns the decoded value of
        a Base64 string base64_authorization_header"""
        if base64_authorization_header is None:
            return None
        if type(base64_authorization_header) is not str:
            return None
        try:
            decoded_string = base64.b64decode(base64_authorization_header)
            return decoded_string.decode("utf-8")
        except Exception as e:
            return None
