# Условие:

# Ваша задача — написать функцию, которая находит сумму всех цифр в числе. На вход также могут пойти и числа меньше нуля — их стоит переводить в неотрицательное числа.

# Пример:

# sumnum(1234) → 10
# sumnum(-9876) → 30
# sumnum(7013) → 11
# sumnum(100001) → 2

import unittest


def sumnum(num: int) -> int:
    return sum([int(i) for i in str(abs(num))])
                
class TestSumNum(unittest.TestCase):
    def test_one(self):
        """ Should return sum num """
        self.assertEqual(10, sumnum(1234))
        self.assertEqual(30, sumnum(-9876))
        self.assertEqual(11, sumnum(7013))
        self.assertEqual(2, sumnum(100001))
 
if __name__ == '__main__':
    unittest.main()
      