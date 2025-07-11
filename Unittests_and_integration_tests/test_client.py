#!/usr/bin/env python3
"""Module to test GithubOrgClient class"""
import unittest
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient
from unittest.mock import patch, PropertyMock


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

    def test_public_repos_url(self):
        """test that _public_repos_url returns a correct payload"""
        test_url = "https://api.github.com/orgs/google/repos"
        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock) as mock_org:
            mock_org.return_value = {"repos_url": test_url}
            client = GithubOrgClient("google")
            result = client._public_repos_url
            self.assertEqual(result, test_url)
