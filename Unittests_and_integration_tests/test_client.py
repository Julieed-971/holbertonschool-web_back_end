#!/usr/bin/env python3
"""Module to test GithubOrgClient class"""
import unittest
from parameterized import parameterized
from utils import get_json
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
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

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """test that the list of repos is the expected one"""
        org_payload, repos_payload, all_names, bsd_names = TEST_PAYLOAD[0]
        test_url = "https://api.github.com/orgs/google/repos"
        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_get_json.return_value = repos_payload
            mock_public_repos_url.return_value = test_url

            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), all_names)
            self.assertEqual(client.public_repos("apache-2.0"), bsd_names)

            mock_get_json.assert_called_once()
            mock_public_repos_url.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license return value"""
        self.assertEqual(GithubOrgClient.has_license(
            repo,
            license_key), expected)
