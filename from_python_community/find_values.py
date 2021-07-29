# Условие:

# Ваша задача — написать функцию, которая принимает неограниченное количество массивов и возвращает только те элементы, что есть в каждом списке.

# Пример:

# find_values([11, 10, 3], [10, 3, 5, 11], [11, 10]) -> [11, 10]
# find_values([8, 4, 7, "hi"], [8, "hi"], [4, "hi"]) -> ['hi']
# find_values([1, 4, 3], [6, 2, 8], ["4", "hi"]) -> []

import unittest


def find_values(*args: list) -> list:
    return sorted(list(set(args[0]).intersection(*args)), reverse=True)

                
class TestFindValues(unittest.TestCase):
    def test_one(self):
        """ Should return items that are in each list """
        self.assertEqual([11, 10], find_values([11, 10, 3], [10, 3, 5, 11], [11, 10]))
        self.assertEqual(['hi'], find_values([8, 4, 7, "hi"], [8, "hi"], [4, "hi"]))
        self.assertEqual([], find_values([1, 4, 3], [6, 2, 8], ["4", "hi"]))

  
if __name__ == '__main__':
    unittest.main()
   