#Условие:

#Ваша задача — написать метод, который будет обрезать строку до определённой длины и добавлять в конец троеточие. 
#Если текст длиннее или же равен max len, то ничего не меняем

import unittest


def cut_str(string: str, max_len: int=10) -> str:
    if len(string) >= max_len:
        return f'{string[:max_len].strip()}...'
    else:
        return string
        
        
class TestCutString(unittest.TestCase):
    def test_one(self):
        """ Should cut string """
        self.assertEqual('Lorem Ipsum...', cut_str('Lorem Ipsum is simply dummy text', 12))
        self.assertEqual('Hello worl...', cut_str('Hello world!'))
        
    def test_two(self):
        """ Should return string """
        self.assertEqual('Lorem Ipsum is simply dummy text', cut_str('Lorem Ipsum is simply dummy text', 40))
if __name__ == '__main__':
    unittest.main()
        