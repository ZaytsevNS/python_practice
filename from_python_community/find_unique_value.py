# Условие:

# Написать функцию, которая будет принимать список и находить уникальное число.

# Пример:

# find_unique_value([1, 2, 1, 1]) -> 2
# find_unique_value([2, 3, 3, 3]) -> 2
# find_unique_value([5, 5, 5, 0.5]) -> 0.5

import unittest
from collections import Counter

def find_unique_value(values: list) -> int:
    counter_values: dict = Counter(values)
    return [k for k, v in counter_values.items() if v == 1][0]

    
class TestFindUniqueValue(unittest.TestCase):
    def test_one(self):
        """ Should return unique value """
        self.assertEqual(2, find_unique_value([1, 2, 1, 1]))
        self.assertEqual(2, find_unique_value([2, 3, 3, 3]))
        self.assertEqual(0.5, find_unique_value([5, 5, 5, 0.5]))
            
if __name__ == '__main__':
    unittest.main()
        