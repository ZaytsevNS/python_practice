# Условие:

# Написать функцию, которая будет возвращать все возможные расположения символов внутри строки 

# Пример:

# permutations("a") -> ['a']
# permutations("ab") -> ['ba', 'ab']
# permutations("abc") -> ['abc', 'cba', 'bca', 'bac', 'cab', 'acb']

import unittest
from itertools import permutations as pm


def permutations(string: str) -> list:
    return sorted(list(''.join(i) for i in set(pm(string))))
        
        
class TestPermutations(unittest.TestCase):
    def test_one(self):
        """ Should return list with permutations """
        self.assertListEqual(['a'], permutations('a'))
        self.assertListEqual(sorted(['ba', 'ab']), permutations('ab'))
        self.assertListEqual(sorted(['abc', 'cba', 'bca', 'bac', 'cab', 'acb']), permutations('abc'))
        
if __name__ == '__main__':
    unittest.main()
        