# package: com.helloworld

import unittest
from com.helloworld.adder import add


class TestAdder(unittest.TestCase):
    def test_positive_numbers(self):
        self.assertEqual(add(2, 3), 5)

    def test_negative_numbers(self):
        self.assertEqual(add(-2, -3), -5)


if __name__ == "__main__":
    unittest.main()
