# Условие:

# Ваша задача — написать функцию, которая перемещает все нули в конец списка. 
# Функция принимает список с набором цифр, а ваша задача — изменить его так, что бы нули оказались в конце списка. 
# Она ничего не возвращает, а лишь меняет полученный список. Порядок ненулевых чисел должен сохранится.

import unittest


def move_zeroes(lst: list) -> list:
    lst[:] = [i for i in lst if i != 0] + [0] * lst.count(0)
    return lst
                
class TestMoveZeroes(unittest.TestCase):
    def test_one(self):
        """ Should return list with zeros at the end of the list """
        self.assertEqual([1, 3, 12, 0, 0], move_zeroes([0, 1, 0, 3, 12]))
        self.assertEqual([1, 3, 5, 0, 0, 0, 0], move_zeroes([1, 0, 3, 0, 0, 0, 5]))
    
    def test_two(self):
        """ Should return list with zero """
        self.assertEqual([0], move_zeroes([0]))

if __name__ == '__main__':
    unittest.main()
   