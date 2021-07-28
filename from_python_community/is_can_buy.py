# Условие:

# На вход идёт словарик типа «Монета : Количество». Монеты могут быть 1, 3, 5 и 10 рублёвыми. Количество монет и цена товара не ограничивается.

# Метод находит суму всех монет и сравнивает цену. Если пользователь может себе позволить товар, то возвращает True, иначе — False.

# Пример:

# moneys = {5: 2, 3 : 2, 1 : 10, 10 : 0}  # sum - 26

# is_can_buy(moneys, 27) → False
# is_can_buy(moneys, 36) → False
# is_can_buy(moneys, 26) → True
# is_can_buy(moneys, 15) → True

import unittest


MONEYS: dict = {5: 2, 3: 2, 1: 10, 10: 0}
def is_can_buy(MONEYS: dict, price: int) -> bool:    
    sum_money: int = sum([k * v for k, v in MONEYS.items()])
    return True if sum_money >= price else False
        
        
class TestIsCanBuy(unittest.TestCase):
    def test_one(self):
        """ Should return True """
        self.assertEqual(True, is_can_buy(MONEYS, 26))
        self.assertEqual(True, is_can_buy(MONEYS, 15))
        
    def test_two(self):
        """ Should return False """
        self.assertEqual(False, is_can_buy(MONEYS, 27))
        self.assertEqual(False, is_can_buy(MONEYS, 36))
        
if __name__ == '__main__':
    unittest.main()
        