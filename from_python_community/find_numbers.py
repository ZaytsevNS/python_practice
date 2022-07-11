# Условие:

# Вам нужно найти все числа внутри строки. Даже те, что находятся внутри слов.

# Пример:

# find_numbers('hello 42 I`m a 32') ➞ ['42', '32']
# find_numbers('bla42bla') ➞ ['42']
# find_numbers('33.33, 1234 1') ➞ ['33', '33', '1234', '1']


import re


def find_numbers(s: str) -> list:
    return re.findall(r'\d+', s)
