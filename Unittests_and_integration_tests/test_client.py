#!/usr/bin/env python3
"""Module to test GithubOrgClient class"""
import unittest
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """Unittest class for GithubOrgClient"""

    @parameterized.expand([
        ('google', {"payload": True}),
        ('abc', {"payload": False})
    ])
    @patch("client.get_json")
    def test_org(self, test_org, expected, mock_get_json):
        """Test that GithubOrgClient returns the correct value"""
        mock_get_json.return_value = expected
        client = GithubOrgClient(test_org)
        result = client.org

        mock_get_json.assert_called_once()
        self.assertEqual(result, expected)
