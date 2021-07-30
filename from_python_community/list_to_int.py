# Условие:

# Ваша задача — написать функцию, которая будет превращать список из нулей и единиц (битов) в целое число.

# Пример:

# list_to_int([0, 0, 0, 1]) -> 1
# list_to_int([0, 1, 0, 1]) -> 5
# list_to_int([1, 1, 1, 1, 1]) -> 31
# list_to_int([1, 1, 1, 1, 0]) -> 30
# list_to_int([1 for _ in range(16)]) -> 65535

import unittest


def list_to_int(arr: list) -> int:
    return int(''.join(str(i) for i in arr), 2)
                
class TestListToInt(unittest.TestCase):
    def test_one(self):
        """ Should return int value """
        self.assertEqual(1, list_to_int([0, 0, 0, 1]))
        self.assertEqual(5, list_to_int([0, 1, 0, 1]))
        self.assertEqual(31, list_to_int([1, 1, 1, 1, 1]))
        self.assertEqual(30, list_to_int([1, 1, 1, 1, 0]))
        self.assertEqual(65535, list_to_int([1 for _ in range(16)]))

if __name__ == '__main__':
    unittest.main()
      