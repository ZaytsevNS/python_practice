# Условие:

# Ваша задача — написать функцию, которая будет проверять, делится ли число на два. Стоит отметить, что использовать операцию / и % нельзя. На вход будет идти и отрицательное и положительное число

# Пример:
# is_even(5) # False
# is_even(-4) # True
# is_even(-3) # False

import unittest
from math import sqrt


def is_even(n):
    return True if str(bin(n))[-1] == '0' else False
    
class TestIsEven(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, is_even(-4))
        self.assertEqual(True, is_even(168))
        self.assertEqual(True, is_even(0))
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, is_even(5))
        self.assertEqual(False, is_even(-3))
        self.assertEqual(False, is_even(-1))
        
if __name__ == '__main__':
    unittest.main()
    