# Условие:
# Вам дан промежуток чисел от 0 от N. Нужно найти сумму всех чисел в этом промежутке, которые делятся на 3 или на 5.

def solution(n: int) -> int:
    return sum(i for i in range(n) if not i % 3 or not i % 5)
