#!/usr/bin/env python3
"""Module of unit and integration tests"""

import unittest
from utils import access_nested_map
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


if __name__ == '__main__':
    unittest.main()
