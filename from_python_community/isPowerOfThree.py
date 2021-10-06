# Условие:

# Ваша задача — написать функцию, которая принимает число и проверяет, является ли оно вознесённой в степень тройкой. 

# Пример:

# isPowerOfThree(27) -> True
# isPowerOfThree(11) -> False
# isPowerOfThree(1) -> True

import unittest
from math import log


def isPowerOfThree(num: int) -> bool:
    #isinstance(log(num, 3), int)
    return True if log(num, 3) % 1 == 0 else False

                
class TestIsPowerOfThree(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, isPowerOfThree(27))
        self.assertEqual(True, isPowerOfThree(1))
    
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, isPowerOfThree(11))   
    
  
if __name__ == '__main__':
    unittest.main()
   