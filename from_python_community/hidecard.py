# Условие:

# На вход идёт строка с номером карты. Она может иметь внутри себя пробелы, что функция и должна предусматривать. Результат — 12 символов * и 4 последних символа от входной строки.

# Пример:

# hidecard("3459 0054 1234 6674") → ************6674
# hidecard("1234567890987654") → ************7654

import unittest


def hidecard(card: str) -> str:
    formatted_number = ''.join(card.split())
    if len(formatted_number) != 16:
        return 'Try again'
    return f'{"*" * 12}{formatted_number[-4:]}'
        
        
class TestHideCard(unittest.TestCase):
    def test_one(self):
        """ Should return hide number """
        self.assertEqual('************6674', hidecard('3459 0054 1234 6674'))
        
    def test_two(self):
        """ Should return hide number """
        self.assertEqual('************7654', hidecard('1234567890987654'))
        
    def test_three(self):
        """ Should return 'Try again' """
        self.assertEqual('Try again', hidecard('4323 2145 3212'))
        
if __name__ == '__main__':
    unittest.main()
        