"""Test reading"""
import unittest
from src.read_db import read_data, format_data


class TestFormatData(unittest.TestCase):

    def test_format_data(self):
        # create some test data
        data = [(1, 'event1', '2022-01-01', 'location1'),
                (2, 'event2', '2022-02-01', 'location2'),
                (3, 'event3', '2022-03-01', 'location3')]

        # call the function with the test data
        result = format_data(data)

        # verify that the output is in the expected format
        self.assertIsInstance(result, tuple)
        self.assertEqual(len(result), 3)
        for row in result:
            self.assertIsInstance(row, tuple)
            self.assertEqual(len(row), 4)
            self.assertIsInstance(row[0], int)
            self.assertIsInstance(row[1], str)
            self.assertIsInstance(row[2], str)
            self.assertIsInstance(row[3], str)

if __name__ == '__main__':
    unittest.main()