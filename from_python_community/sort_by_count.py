# Условие:

# Необходимо написать функцию, которая будет принимать два массива. Её задача — отсортировать элементы из первого массива, в зависимости от их повторяемости в втором.

import unittest


def sort_by_count(list1: list, list2: list) -> list:
    return sorted(list1, key=lambda x: list2.count(x), reverse=True)
                    
class TestSortByCount(unittest.TestCase):
    def test_one(self):
        """ Should return sorted list """
        self.assertEqual([3, 0, 'b'], sort_by_count(['b', 0, 3], ['a', 0, 1, 1, 3, 1, 3]))
        self.assertEqual([1, 3, 2], sort_by_count([1, 2, 3], [1, 1, 1, 1, 2, 3, 3, 3]))
        self.assertEqual([1, 0, None], sort_by_count([None, 0, 1], ['a', 0, 1, 1, 3, 1, 3]))
    
if __name__ == '__main__':
    unittest.main()
   