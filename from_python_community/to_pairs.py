# Условие:

# Напишите, пожалуйста, функцию, которая превращает одномерный список в список из пар. 

# Если количество элементов в списке не позволяет поделить его на 2, то метод использует необязательный метод fill_char с значением для заполнения.

# Желательно не использовать сторонние модули.

# Пример:

# to_pairs([1, 2, 3, 4]) -> [[1, 2], [3, 4]]
# to_pairs([1, 2, 3, 4, 5]) -> [[1, 2], [3, 4], [5, None]]
# to_pairs([1, 2, 3, 4, 5, 0], fill_char = 0) -> [[1, 2], [3, 4], [5, 0]]

import unittest


def to_pairs(arr: list, fill_char=None) -> list:
    pairs: list = []
    if len(arr) % 2:
        arr.append(fill_char)
    for i in range(0, len(arr), 2):
        pairs.append(arr[i:i+2])
    return pairs
                
class TestToPairs(unittest.TestCase):
    def test_one(self):
        """ Should return list with pairs """
        self.assertEqual([[1, 2], [3, 4]], to_pairs([1, 2, 3, 4]))
        self.assertEqual([[1, 2], [3, 4], [5, None]], to_pairs([1, 2, 3, 4, 5]))
        self.assertEqual([[1, 2], [3, 4], [5, 0]], to_pairs([1, 2, 3, 4, 5, 0]))

if __name__ == '__main__':
    unittest.main()
   