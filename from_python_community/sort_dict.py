# Условие:

# Ваша задача — написать функцию, которая сортирует словарь по убываю на основе значения.

# Пример:

# sort_dict({"1": 1, "2": 2, "3": 3}) -> {"3": 3, "2": 2, "1": 1}
# sort_dict({"obj": 8, 1: 11, "6": 4}) -> {1: 11, "obj": 8, "6": 4}

import unittest


def sort_dict(d: dict) -> dict:
    sorted_d: dict = dict(sorted(d.items(), key=lambda x: x[1], reverse=True))
    return sorted_d
        
        
class TestSortDict(unittest.TestCase):
    def test_one(self):
        """ Should return sorted dict """
        self.assertEqual({"3": 3, "2": 2, "1": 1}, sort_dict({"1": 1, "2": 2, "3": 3}))
        self.assertEqual({1: 11, "obj": 8, "6": 4}, sort_dict({"obj": 8, 1: 11, "6": 4}))
        
if __name__ == '__main__':
    unittest.main()
        