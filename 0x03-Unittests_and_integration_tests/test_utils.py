#!/usr/bin/env python3

"""
Parameterize a unit test
Create a TestAccessNestedMap class
that inherits from unittest.TestCase.
Implement the TestAccessNestedMap.test_access_nested_map method
to test that the method returns what it is supposed to
"""

import unittest
import parameterized import parameterized
from utils import access_nested_map, get_json, memoize
from unittest.mock import patch, Mock


class TestAccessNestedMap(unittest.TestCase):
    """
    Implement the TestAccessNestedMap.test_access_nested_map
    method to test that the method returns what it is supposed to
    """
    @parameterized.expand(
            [
                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2)
            ]
            )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """summary"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)

        @parameterized.expand(
                [
                    ({}, ("a",), KeyError),
                    ({"a": 1}, ("a", "b"), KeyError)
                ]
            )
    def test_access_nested_map_exception(self, nested_map, path,
                                         expected_output):
        """Raise exception"""
        with self.assertRaises(expected_output) as context:
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Mocking HTTP Calls"""

    @parameterized.expand(
            [
                ("http://example.com", test_payload={"payload": True}),
                ("http://holberton.io", test_payload={"payload": False})
                ]
            )
    def test_get_json(self, url, expected_output):
        """summary get json"""
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch('request.get', return_value=mock_response):
            response = get_json(url)
            self.assertEqual(response, expected_output)


class TestMemoize(unittest.TestCase):
    """
    summary memoization
    """

    def test_momize(self):
        """
        __summary__

        Returns:
        __type__:__description__
        """

        class TestClass:
            """
            __summary__
            """

            def a_method(self):
                """
                __summary__
                """
                return 42

            @memoize
            def a_property(self):
                """
                game
                """
                return self.a_method()

            test_obj = TestClass()

            with patch.object(test_obj, 'a_method') as mock_method:
                mock_method.return_value = 42

                res = test_obj.a_property
                res1 = test_obj.a_property

                self.assertEqual(res, 42)
                self.assertEqual(res1, 42)
                mock_method.assert_called_once()
