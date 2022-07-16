# Условие:

# Знаете, в автобусах раздают билеты с номерами. Если сумма цифр первой половины равна сумме цифр второй половины, то билет — счастливый. 

# Если длина строки не делится нацело на два, то цифру посередине игнорируем. На вход идёт строка только из чисел.

# Примеры:

# luck_check('56328116') ➞ True
# luck_check('123456') ➞ False
# luck_check('17935') ➞ True


def luck_check(num: str) -> bool:
    half: int = len(num) // 2
    sum_left_half: int = sum(map(int, num[:half]))
    if len(num) % 2:
        half += 1
    sum_right_half: int = sum(map(int, num[half:]))
    return sum_left_half == sum_right_half
