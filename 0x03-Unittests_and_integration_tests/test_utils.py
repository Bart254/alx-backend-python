#!/usr/bin/env python3
"""Unittest implementation module"""
import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """ test class for access_nested_map"""
    @parameterized.expand([
        ({"a": 1}, ('a',), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, map, keys, output):
        """ test case for method access_nested_map"""
        self.assertEqual(access_nested_map(map, keys), output)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, map, keys):
        """ test exceptions for access_nested_map"""
        with self.assertRaises(KeyError) as err:
            access_nested_map(map, keys)
