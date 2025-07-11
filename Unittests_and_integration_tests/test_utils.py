#!/usr/bin/env python3
"""Module of unit and integration tests"""

import unittest
from unittest.mock import patch, PropertyMock, Mock
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)


class TestAccessNestedMap(unittest.TestCase):
    """Class containing unittests"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test method to assert result of the access_nested_map method"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected)

    @parameterized.expand([
        ({}, ("a")),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test method to assert the exception raised by access_nested_map"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class containing unittests to test get_json method"""
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """Method to test the get_json method"""
        with patch('utils.requests.get') as mock_request_get:
            mock_response = Mock()
            mock_response.json.return_value = test_payload
            mock_request_get.return_value = mock_response

            response = get_json(test_url)
            mock_request_get.assert_called_once_with(test_url)

            self.assertEqual(response, test_payload)


class TestMemoize(unittest.TestCase):
    """Class containing unittests to test memoized method"""
    def test_memoize(self):
        """Method to test the memoize method"""
        class TestClass:
            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        test = TestClass()
        with patch.object(TestClass,
                          'a_method',
                          return_value=42) as mock_a_method:
            result1 = test.a_property
            result2 = test.a_property
            self.assertEqual(result1, result2)
            mock_a_method.assert_called_once


if __name__ == '__main__':
    unittest.main()
