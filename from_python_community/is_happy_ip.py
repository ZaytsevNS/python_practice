# Условие:

# Найти «счастливый» ip. Он считается счастливым, если сумма двух байтов с левой стороны равняются сумме двух байтов с правой стороны. 

# На вход функции всегда идёт строка с ipv4 адресом.

# Пример:
# is_happy_ip("255.255.255.255") -> True
# is_happy_ip("0.0.0.1") -> False
# is_happy_ip("101.78.170.9") -> True

import unittest


def is_happy_ip(ip: str) -> bool:
    list_num = [int(i) for i in ip.split('.')]
    if len(list_num) < 4:
        return False
    if sum(list_num[0:2]) == sum(list_num[2:4]):
        return True
    return False
    
class TestIsHappyIp(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, is_happy_ip('255.255.255.255'))
        self.assertEqual(True, is_happy_ip('101.78.170.9'))
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, is_happy_ip('0.0.0.1'))
        self.assertEqual(False, is_happy_ip('1.2.3'))

if __name__ == '__main__':
    unittest.main()
