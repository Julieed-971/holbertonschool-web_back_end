#!/usr/bin/env python3
"""Module to test GithubOrgClient class"""
import unittest
import requests
from parameterized import parameterized, parameterized_class
from utils import get_json
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from unittest.mock import patch, PropertyMock, Mock

org_payload, repos_payload, expected_repos, apache2_repos = TEST_PAYLOAD[0]
test_url = "https://api.github.com/orgs/google/repos"


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

        with patch(
                "client.GithubOrgClient._public_repos_url",
                new_callable=PropertyMock) as mock_public_repos_url:
            mock_get_json.return_value = repos_payload
            mock_public_repos_url.return_value = test_url

            client = GithubOrgClient("google")
            self.assertEqual(client.public_repos(), expected_repos)
            self.assertEqual(client.public_repos("apache-2.0"), apache2_repos)

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


@parameterized_class(
    ('org_payload', 'repos_payload', 'expected_repos', 'apache2_repos'),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test for GithubOrgClient"""

    @classmethod
    def setUpClass(cls):
        """Set up the test class by patching requests.get"""
        cls.ORG_URL = GithubOrgClient.ORG_URL
        cls.get_patcher = patch('requests.get')
        mock_get = cls.get_patcher.start()

        def get_mock(url):
            mock_response = Mock()
            if url == cls.ORG_URL.format(org="google"):
                mock_response.json.return_value = cls.org_payload
            elif url == cls.org_payload["repos_url"]:
                mock_response.json.return_value = cls.repos_payload
            else:
                mock_response.json.return_value = None
            return mock_response

        mock_get.side_effect = get_mock

    @classmethod
    def tearDownClass(cls):
        """Tear down the test class by stopping the patcher"""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Integration test for public_repos"""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)
        self.assertEqual(client.public_repos("apache-2.0"), self.apache2_repos)
