# Условие:

# Ваша задача — написать функцию, которая переводит многомерный массив в одномерный

# Пример:

# to_one_dimension_list([1, [2, 3, [4,5], 6]]) -> [1, 2, 3, 4, 5, 6]
# to_one_dimension_list([1, 2, 3]) -> [1, 2, 3]
# to_one_dimension_list([1, [[3]], 5])  -> [1, 3, 5]

import unittest


def to_one_dimension_list(arr: list) -> list:
    flatten_arr: list = []
    for i in arr:
        if isinstance(i, list):
            flatten_arr.extend(to_one_dimension_list(i))
        else:
            flatten_arr.append(i)
    return flatten_arr
                
class TestToOneDimensionList(unittest.TestCase):
    def test_one(self):
        """ Should return one dimension list """
        self.assertEqual([1, 2, 3, 4, 5, 6], to_one_dimension_list([1, [2, 3, [4,5], 6]]))
        self.assertEqual([1, 2, 3], to_one_dimension_list([1, 2, 3]))
        self.assertEqual([1, 3, 5], to_one_dimension_list([1, [[3]], 5]))
  
if __name__ == '__main__':
    unittest.main()
   