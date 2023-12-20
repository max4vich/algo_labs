import unittest

from andrew_counts import andrewCounts


class TestFindThreeNumbers(unittest.TestCase):

    def test_find_three_numbers(self):
        self.assertEqual(andrewCounts([1, 2, 3], 6), True)


if __name__ == '__main__':
    unittest.main()