# Условие:

# Написать простую функцию, которая будет возвращать век, на основе года.

# Пример:

# get_century(2021) -> 21
# get_century(1999) -> 20
# get_century(2000) -> 20
# get_century(101) -> 2

import unittest


def get_century(n: int) -> int:
    a, b = divmod(n, 100)
    return a + 1 if b > 0 else a

class TestGetCentury(unittest.TestCase):
    def test_one(self):
        """ Should return century """
        self.assertEqual(21, get_century(2021))
        self.assertEqual(20, get_century(1999))
        self.assertEqual(20, get_century(2000))
        self.assertEqual(2, get_century(101))
  
if __name__ == '__main__':
    unittest.main()
   