# Условие:
# Нужно перевести RGB в HEX формат.

# Пример:
# rgb_to_hex(255, 255, 255) ➞ 'FFFFFF'
# rgb_to_hex(127, 13, 253) ➞ '7F0DFD'
# rgb_to_hex(0, 0, 0) ➞ '000000'


def rgb_to_hex(*args) -> str:
    a, b, c = args
    if len(args) == 3 and 0 <= a <= 255 and 0 <= b <= 255 and 0 <= c <= 255:
        return f'{a:02x}{b:02x}{c:02x}'.upper()
    return 'Wrong value'
