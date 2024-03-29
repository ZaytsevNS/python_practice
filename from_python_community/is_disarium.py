# Условие:
# Создайте функцию, которая определяет, является ли число дисариумом или нет. 
# Число называется дисариумом, если сумма его цифр, возведенных в соответствующие положения, равна самому числу.

# Пример:

# is_disarium(75) ➞ False
# 7 ** 1 + 5 ** 2 = 7 + 25 = 32

# is_disarium(135) ➞ True
# 1 ** 1 + 3 ** 2 + 5 ** 3 = 1 + 9 + 125 = 135

def is_disarium(num: int) -> bool:
    s = 0
    for i, k in enumerate(str(num), 1):
        s += int(k)**i
    return s == num
