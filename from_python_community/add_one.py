# Ваша задача — написать функцию, которая принимает список из цифр, которые являются одним числом.
# Ей необходимо добавить к числу 1. В результате функция возвращает список из цифр.


def add_one(num: list) -> list:
    return [int(i) for i in str(int(''.join(map(str, num))) + 1)]

num = [1,2,3,4,5]
print(add_one(num))
