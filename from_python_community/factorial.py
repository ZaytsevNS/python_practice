# Условие:

# Ваша задача на этот раз — просто написать функцию для просчёта факториала. 

# Пример:

# factorial(10) -> 3628800
# factorial(3) -> 6
# factorial(1) -> 1
# factorial(-1) -> 1

import unittest


def factorial(n: int) -> int:
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
                
class TestFactorial(unittest.TestCase):
    def test_one(self):
        """ Should return factorial value"""
        self.assertEqual(3628800, factorial(10))
        self.assertEqual(6, factorial(3))
        self.assertEqual(1, factorial(1))
        
    def test_two(self):
        """ Should return 1 """
        self.assertEqual(1, factorial(-1))
                
if __name__ == '__main__':
    unittest.main()
        