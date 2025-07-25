#!/usr/bin/env python3
"""Module for basic authentication"""
from api.v1.auth.auth import Auth
from models.user import User
import base64
from typing import TypeVar


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

    def extract_user_credentials(
            self,
            decoded_base64_authorization_header: str) -> (str, str):
        """returns the user email and password from the Base64 decoded value"""
        if decoded_base64_authorization_header is None:
            return None, None
        if type(decoded_base64_authorization_header) is not str:
            return None, None
        if ":" not in decoded_base64_authorization_header:
            return None, None
        separator_index = decoded_base64_authorization_header.find(":")
        if separator_index:
            email = decoded_base64_authorization_header[:separator_index]
            password = decoded_base64_authorization_header[(separator_index
                                                            + 1):]
            return email, password

    def user_object_from_credentials(
            self,
            user_email: str,
            user_pwd: str) -> TypeVar('User'):
        """returns the User instance based on his email and password."""
        if type(user_email) is not str or type(user_pwd) is not str:
            return None
        user = User()
        user.load_from_file()
        found_user = user.search({'email': user_email})
        if not found_user:
            return None
        if found_user[0].is_valid_password(user_pwd):
            return found_user[0]
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """overloads Auth and retrieves the User instance for a request"""
        if request is not None:
            auth_header = self.authorization_header(request)
            if auth_header is not None:
                base64_auth_header = self.extract_base64_authorization_header(
                    auth_header)
                decoded_header = self.decode_base64_authorization_header(
                    base64_auth_header)
                email, password = self.extract_user_credentials(
                    decoded_header)
                return self.user_object_from_credentials(email, password)
        return None
