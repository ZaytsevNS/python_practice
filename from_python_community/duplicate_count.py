# Условие:
# Нужно подсчитать количество повторяющихся символов в строке.

# Пример:
# duplicate_count('abcde') ➞ 0      
# duplicate_count('aabbcde') ➞ 2  # a and b
# duplicate_count('ABBBac') ➞ 2    # a and b

import unittest
from collections import Counter


def duplicate_count(string: str) -> int:
    counter: dict = Counter(string.lower())
    return sum(1 for v in counter.values() if v > 1)

class TestDuplicateCount(unittest.TestCase):

    def test_one(self):
        self.assertEqual(duplicate_count('abcde'), 0)
        self.assertEqual(duplicate_count('aabbcde'), 2)
        self.assertEqual(duplicate_count('ABBBac'), 2)

if __name__ == '__main__':
    unittest.main()
