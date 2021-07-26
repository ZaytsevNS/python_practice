# Условие:

# Ваша задача — найти суму всех чисел, перемноженных на их индекс.

# Пример:

# sum_mult_index([1,2,3,4]) -> 20
# sum_mult_index([11,22,55,33,44]) -> 407
# sum_mult_index([-1, 0, -8, 11]) -> 17
# sum_mult_index([0, 0, 0, 0, 0]) -> 0

import unittest


def sum_mult_index(num: list) -> int:
    return sum([i * k for i, k in enumerate(num)])
                
class TestCutString(unittest.TestCase):
    def test_one(self):
        """ Should return sum """
        self.assertEqual(20, sum_mult_index([1,2,3,4]))
        self.assertEqual(407, sum_mult_index([11,22,55,33,44]))
        self.assertEqual(17, sum_mult_index([-1, 0, -8, 11]))
        self.assertEqual(0, sum_mult_index([0, 0, 0, 0, 0]))

if __name__ == '__main__':
    unittest.main()
        