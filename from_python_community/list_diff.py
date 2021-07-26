# Условие:

# Ваша задача — написать функцию, которая будет находить отличия между первым и вторым списком

# Пример:

# list_diff([], []) -> []
# list_diff([], [1, 2]) -> []
# list_diff([1, 2], [2]) -> [1]
# list_diff([6, 4, 3], [7]) -> [6, 4, 3]

import unittest


def list_diff(list_one: list, list_two: list) -> list:
    return [i for i in list_one if i not in list_two]
    
class TestListDiff(unittest.TestCase):
    def test_one(self):
        """ Should return empty list """
        self.assertEqual([], list_diff([], []))
        self.assertEqual([], list_diff([], [1, 2]))
    
    def test_two(self):
        """ Should return list with elements """
        self.assertEqual([1], list_diff([1, 2], [2]))
        self.assertEqual([6, 4, 3], list_diff([6, 4, 3], [7]))
        
if __name__ == '__main__':
    unittest.main()
