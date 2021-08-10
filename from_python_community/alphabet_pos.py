# Условие:

# Ваша задача — написать функцию, которая будет возвращать список из позиций букв в алфавите.

import unittest
from string import ascii_lowercase


def alphabet_pos(string: str) -> list:
    if string:
        dict_letter = {v:k for k, v in enumerate(ascii_lowercase, start=1)}
        return [dict_letter.get(i.lower()) for i in string if i.lower() in ascii_lowercase]
    return []
                
class TestAlphabetPos(unittest.TestCase):
    def test_one(self):
        """ Should return list with alphabet pos """
        self.assertEqual([8, 9, 16, 25, 20, 8, 15, 14, 3, 15, 13, 13, 21, 14, 9, 20, 25], alphabet_pos('Hi python community!'))
        self.assertEqual([15, 8, 14, 15], alphabet_pos('oh, no!!\n\t'))
    
    def test_two(self):
        """ Should return empty list """
        self.assertEqual([], alphabet_pos('123 \n'))
        self.assertEqual([], alphabet_pos(''))

if __name__ == '__main__':
    unittest.main()
   