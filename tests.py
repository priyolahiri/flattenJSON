import json
import unittest

from main import flatten


class UnitTests(unittest.TestCase):
    def test_simple_input(self):
        """
        Test to check results with simple one-level hierarchical json
        """
        with open('files/input.json', 'r') as f:
            json_data = json.load(f)
        result = flatten(json_data)
        expected = {'a': 1, 'b': True, 'c.d': 3, 'c.e': 'test'}
        self.assertEqual(result, expected)

    def test_advanced_input(self):
        """
        Test to check results with advanced two-level hierarchical json
        """
        with open('files/input_2.json', 'r') as f:
            json_data = json.load(f)
        result = flatten(json_data)
        expected = {'a': 1, 'b': True, 'c.d': 3, 'c.e': 'test', 'f.g.h': 'deep test', 'f.g.i': 10}
        self.assertEqual(result, expected)

    def test_list_input(self):
        """
        Test to check if a json file with arrays is rejected
        """
        with open('files/input_list.json', 'r') as f:
            json_data = json.load(f)
        with self.assertRaises(Exception):
            flatten(json_data)


if __name__ == '__main__':
    unittest.main()