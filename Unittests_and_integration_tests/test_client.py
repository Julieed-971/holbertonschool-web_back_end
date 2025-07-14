#!/usr/bin/env python3
"""Module to test GithubOrgClient class"""
import unittest
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
    ('org_payload, repos_payload, expected_repos, apache2_repos'), TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """test class to create integration test for GithubOrgClient"""
    @classmethod
    def setUpClass(GithubOrgClient):
        """Set up the test class"""
    # should mock requests.get to return example payloads found in the fixtures.
    # Use patch to start a patcher named get_patcher, and use side_effect
    # to make sure the mock of requests.get(url).json() returns the correct
    # fixtures for the various values of url that you anticipate to receive.
        with patch('utils.requests.get') as mock_requests_get:
            mock_response = Mock()
            mock_response.json.return_value = TEST_PAYLOAD[0][1]
            mock_requests_get.return_value = mock_response
            
            response = get_json(test_url)
            GithubOrgClient.assertEqual(response, TEST_PAYLOAD[0][1])
            
        get_patcher = patch('__main__.GithubOrgClient', spec=True)
        MockClass = get_patcher.start()
        instance = MockClass()
        instance.org.json(org=test_url).side_effect = TEST_PAYLOAD[0][1]

    @classmethod
    def tearDownClass(GithubOrgClient):
        """Tear down the test class"""
        TestIntegrationGithubOrgClient.setUpClass.get_patcher.stop()
        