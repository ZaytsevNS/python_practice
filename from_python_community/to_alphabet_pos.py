# Условие:

# Вам нужно превратить строку в список, состоящий из порядкового номера каждой буквы ('a' = 1, 'b' = 2). Игнорируйте # регистр и пропускайте символы, не входящие в алфавит.

# Набор символы английского алфавита можно найти в string.ascii_letters.

# Пример:

# to_alphabet_pos('a-z') -> [1, 26]
# to_alphabet_pos('S p A C/ e') -> [19, 16, 1, 3, 5]
# to_alphabet_pos('1!60:)7&') -> []

from string import ascii_lowercase

def to_alphabet_pos(s: str) -> list:
    english: dict = {v:k for k,v in enumerate(ascii_lowercase, 1)}
    return [english.get(i.lower()) for i in s if i.lower() in ascii_lowercase]
