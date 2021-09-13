# Условие:

# Написать функцию, которая будет возвращать все числа, на которые делится аргумент функции. Если же аргумент — простое число, то возвращаем строку, как на примере.

# Пример:

# find_divisors(13) -> 13 - простое число
# find_divisors(10) -> [2, 5]
# find_divisors(12) -> [2, 3, 4, 6]

import unittest
from math import floor, sqrt


def is_prime_number(n: int) -> bool:
    if not n % 2 and n != 2:
        return False
    flag = True
    for i in range(3, floor(sqrt(n)) + 1, 2):
        if not n % i:
            flag = False
            break
    return flag

def find_divisors(n: int):
    if is_prime_number(n) == True:
        return f'{n} - простое число'
    else:
        return [i for i in range(2, n // 2 + 1) if not n % i]


class TestFindDivisors(unittest.TestCase):
    def test_one(self):
        """ Should return string """
        self.assertEqual('13 - простое число', find_divisors(13))
        
    def test_two(self):
        """ Should return list with divisors """
        self.assertEqual([2, 5], find_divisors(10))
        self.assertEqual([2, 3, 4, 6], find_divisors(12))
  
if __name__ == '__main__':
    unittest.main()
   