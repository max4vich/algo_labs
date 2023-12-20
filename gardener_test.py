import unittest
import gardener


class TestGardener(unittest.TestCase):
    def test_5_5(self):
        expected_result = [1, 2, 3, 4, 5,
                           10, 9, 8, 7, 6,
                           11, 12, 13, 14, 15,
                           20, 19, 18, 17, 16,
                           21, 22, 23, 24, 25]
        self.assertEqual(gardener.gardener_count(5, 5), expected_result)

    def test_2_4(self):
        expected_result = [1, 2, 3, 4,
                           8, 7, 6, 5]
        self.assertEqual(gardener.gardener_count(2, 4), expected_result)

    def test_6_1(self):
        expected_result = [1, 2, 3, 4, 5, 6]
        self.assertEqual(gardener.gardener_count(6, 1), expected_result)


if __name__ == "__main__":
    unittest.main()
