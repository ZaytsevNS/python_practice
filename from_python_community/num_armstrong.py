def num_armstrong(num: int) -> bool:
    if 1 <= num < 10:
        return True
    power = len(str(num))
    return True if sum([pow(int(i), power) for i in str(num)]) == num else False
