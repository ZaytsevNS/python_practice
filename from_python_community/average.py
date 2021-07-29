# Условие:

# Ваша задача — написать код, который получает словарик типа «Имя : [массив оценок]».

# Необходимо среди всех значений словаря найти ученика с максимальным и минимальным средним баллом, а после — вывести его имя вместе со средним балом.

# Пример:

# Вход: {"Mark":[2, 6, 9, 2], "Kevin": [11, 8], "John":[7, 4, 11, 5, 8], "Max": [2, 4, 5]}

# Вывод: Kevin: 9.5\nMax: 3.67

import unittest

STUDENT: dict = {"Mark": [2, 6, 9, 2], "Kevin": [11, 8], "John": [7, 4, 11, 5, 8], "Max": [2, 4, 5]}
def average(STUDENT: dict) -> str:
    max_value = max([sum(v) / len(v) for v in STUDENT.values()])
    list_with_max_value = [v for v in STUDENT.values() if sum(v) / len(v) == max_value]
    min_value = min([sum(v) / len(v) for v in STUDENT.values()])
    list_with_min_value = [v for v in STUDENT.values() if sum(v) / len(v) == min_value]
    return f'{", ".join(sorted([k for k, v in STUDENT.items() if v in list_with_max_value]))}: {round(max_value, 2)}\n{", ".join(sorted([k for k, v in STUDENT.items() if v in list_with_min_value]))}: {round(min_value, 2)}'
                
class TestAverage(unittest.TestCase):
    def test_one(self):
        """ Should return string with max and min average scores """
        self.assertEqual('Kevin: 9.5\nMax: 3.67', average(STUDENT))
  
if __name__ == '__main__':
    unittest.main()
   