# Условие:
# Необходимо проверить, является ли слово - изограммой - то, в котором не повторяется ни одна буква.

# Примеры:
# is_isogram('Dermatoglyphics') -> True
# is_isogram('isogram') -> True
# is_isogram('aba') -> False
# is_isogran('') -> True

def is_isogram(word: str) -> bool:
    return len(word) == len(set(word.lower()))
    
print(is_isogram('Dedrmatoglyphics'))