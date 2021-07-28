# Условие:

# Ваша задача — написать функцию, которая будет переводить CamelCase и Lower CamelCase в Lowercase с подчеркиванием.

# Пример:

# change_to_lower("variableName") -> variable_name
# change_to_lower("test") -> test

import unittest


def change_to_lower(string: str) -> str:
    if string.islower():
        return string
    modified_str: str = ''
    for i, k in enumerate(string):
        if k.isupper() and i == 0:
            modified_str += k.lower()
        elif k.isupper():
            modified_str += f'_{k.lower()}'
        else:
            modified_str += k
    return modified_str
    
class TestChangeToLower(unittest.TestCase):
    def test_one(self):
        """ Should return modified string """
        self.assertEqual('variable_name', change_to_lower('variableName'))
        self.assertEqual('variable_name', change_to_lower('VariableName'))
        self.assertEqual('variable1_name', change_to_lower('Variable1Name'))
        self.assertEqual('camel_case_string1', change_to_lower('CamelCaseString1'))
        
    def test_two(self):
        """ Should return original string """
        self.assertEqual('test', change_to_lower('test'))
        self.assertEqual('testtest', change_to_lower('testtest'))
        
if __name__ == '__main__':
    unittest.main()
        