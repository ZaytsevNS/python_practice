# Условие:

# Ваша цель — написать функцию, которая находит недостающие буквы английского алфавита. 

# На вход идут только символы английского языка в нижнем регистре. Возвращаемое значение — строка из недостающих символов.

# Пример:

# findmissingletters('abc') -> defghijklmnopqrstuvwxyz
# findmissingletters('mnopqrstuvwxyz') -> abcdefghijkl
# findmissingletters('acegikmoqsuwy') -> bdfhjlnprtvxz

import unittest
from string import ascii_letters


def findmissingletters(letters: str) -> str:
    if letters:
        return ''.join(sorted(set(ascii_letters) - set(letters)))
    return ''
        
        
class TestFindMissingLetters(unittest.TestCase):
    def test_one(self):
        """ Should return missing letters """
        self.assertEqual('BCDEFGHIJKLMNOPQRSTUVWXYZdefghijklmnopqrstuvwxyz', findmissingletters('aaAbc'))
        self.assertEqual('abcdefghijkl', findmissingletters('ABCDEFGHIJKLMNOPQRSTUVWXYZmnopqrstuvwxyz'))
        self.assertEqual('ABDEFGHIJKLNOPQRSTUVWXYZbdfhjlnprtvxz', findmissingletters('acCCegikmMoqsuwy'))
        
    def test_two(self):
        """ Should returns empty string """
        self.assertEqual('', findmissingletters(''))
        
if __name__ == '__main__':
    unittest.main()
        