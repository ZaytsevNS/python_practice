# Условие:

# Ваша задача — написать функцию, которая проверяет, является ли число простым.
# Простые числа — числа, которые делятся нацело только на единицу и на само себя.

import unittest
from math import sqrt, floor


def is_prime_number(n: int) -> bool:
    if not n % 2 and n != 2:
        return False
    flag = True
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if not n % i:
            flag = False
            break
    return flag
               
class TestIsPrimeNumber(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, is_prime_number(1))
        self.assertEqual(True, is_prime_number(2))
        self.assertEqual(True, is_prime_number(3))
        self.assertEqual(True, is_prime_number(53))
        self.assertEqual(True, is_prime_number(127))
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, is_prime_number(9))
        self.assertEqual(False, is_prime_number(117))
        self.assertEqual(False, is_prime_number(124))
        self.assertEqual(False, is_prime_number(522))
        
          
if __name__ == '__main__':
    unittest.main()
   