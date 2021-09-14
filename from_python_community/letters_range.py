# Условие:

# Написать функцию, которая будет принимать диапазон букв, разделённых дефисом и возвращать все символы между ними включительно.

# Никаких проверок на ошибку делать не надо, минимальное значение всегда меньше или равно максимальному.

# Пример:

# letters_range("a-c") -> abc
# letters_range("a-a") -> a
# letters_range("s-H") -> stuvwxyzABCDEFGH
# letters_range("a-A") -> abcdefghijklmnopqrstuvwxyzA

import unittest
from string import ascii_letters as letters


def letters_range(let_range: str) -> str:
    let_range = let_range.split('-')
    return letters[letters.index(let_range[0]):letters.index(let_range[1])+1]
                
class TestLettersRange(unittest.TestCase):
    def test_one(self):
        """ Should return string with letters """
        self.assertEqual('abc', letters_range('a-c'))
        self.assertEqual('a', letters_range('a-a'))
        self.assertEqual('stuvwxyzABCDEFGH', letters_range('s-H'))
        self.assertEqual('abcdefghijklmnopqrstuvwxyzA', letters_range('a-A'))
  
if __name__ == '__main__':
    unittest.main()
   