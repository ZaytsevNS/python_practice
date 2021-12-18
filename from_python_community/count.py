# Подсчитывает количество положительных и отрицательных чисел

# count([5,4,1,2,-1,2]) -> (4,2)
# [1,0,-1] -> (1,1)
# [0,0,0,0] -> (0,0)

def count(numbers: list) -> tuple:
    positive = len(list(filter(lambda i: i > 0, numbers)))
    negative = len(list(filter(lambda i: i < 0, numbers)))
    return (positive, negative)
