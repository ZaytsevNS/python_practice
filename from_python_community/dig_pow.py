# Условие:

# Вам нужно каждую цифру из полученного числа возвести в степень его порядкового номера.

# Примеры:

# dig_pow(89) -> 89      # 8^1 + 9^2 
# dig_pow(695) -> 212  # 6^1 + 9^2 + 5^3
# dig_pow(100) -> 1

def dig_pow(n: int) -> int:
    return sum(int(k)**i for i, k in enumerate(str(n), 1))

        
print(dig_pow(100))
