# Условие:

# Ваша задача — написать функцию, которая просчитывает счёт игроков и определяет, кто победил. На вход идёт войско двух команд (два аргумента) в виде списка.

# Каждое войско даёт разную силу. Воин — 1, лучник — 2, Гигант — 5, волшебник — 10. Тип героя зависит от индекса. Функция возвращает текст с победившей командой или ничью, если счёт равен.

import unittest
from numpy import prod


SKILL = [1, 2, 5, 10]
def who_won(team1: list, team2: list) -> str:
    points_team1: int = sum(list(map(prod, zip(team1, SKILL))))
    points_team2: int = sum(list(map(prod, zip(team2, SKILL))))
    if points_team1 > points_team2:
        return "Команда1 победила"
    elif points_team1 < points_team2:
        return "Команда2 победила"
    else:
        return "Ничья"
                
class TestWhoWon(unittest.TestCase):
    def test_one(self):
        self.assertEqual("Команда1 победила", who_won([6, 4, 3, 1], [12, 0, 0, 1]))
        self.assertEqual("Команда2 победила", who_won([1, 1, 1, 0], [0, 0, 1, 1]))
        self.assertEqual("Ничья", who_won([1, 1, 1, 1], [1, 1, 1, 1]))

if __name__ == '__main__':
    unittest.main()
   