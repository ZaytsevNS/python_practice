# Условие:

# Ваша задача — написать функцию, которая проверяет, правильно ли записаны скобочки в полученной строке. 
# Строка состоит только из символа "(" и ")", никаких проверок делать не нужно.

def solution(s: str) -> bool:
    try:
        eval(s)
        return True
    except SyntaxError:
        return False

s = '())'
print(solution(s))