# Условие:

# Ваша цель — написать функцию, которая находит самые повторяющиеся слова в строке.

# Пример:

# text ('Am I want write code? Yeah! I like it') → I
# text ('Hi! How are you? Hi! I am ok') → Hi
# text ('test text test and test that again') → test

import unittest
from collections import Counter


def text(string: str) -> str:
    formatted_string = string.replace('!', '').replace('?', '').replace('.', '').replace('...', '')
    word: dict = dict(Counter([i for i in formatted_string.split()]))
    max_value: int = max([i for i in word.values()])
    return ', '.join(sorted([k for k, v in word.items() if v == max_value], key=len))
                
class TestText(unittest.TestCase):
    def test_one(self):
        """ Should return one value """
        self.assertEqual('I', text('Am I want write code? Yeah! I like it'))
        self.assertEqual('Hi', text('Hi! How are you? Hi! I am ok'))
        self.assertEqual('test', text('test text test and test that again'))

    def test_two(self):
        """ Should return two values """
        self.assertEqual('tes, text', text('text text tes and tes that again'))    

if __name__ == '__main__':
    unittest.main()
      