# Принимает список из целых чисел и возвращает то, что повторяется нечетное кол-во раз

# [7] -> 7
# [0, 1, 0] -> 1
# [0, 1, 0, 1, 0] -> 0


from collections import Counter


def get(num: list):
    counter: dict = Counter(num)
    return [k for k, v in counter.items() if v % 2][0]
