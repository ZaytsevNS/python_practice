# Вам нужно узнать, является ли предложение панграммой?
# Это предложения, в котором используются все буквы алфавита как минимум раз.

# is_pangram('The quick brown fox jumps over a lazy dog') -> True
# is_pangram('Sphinx of black quartz, judge my vow') -> True
# is_pangram('not pangram') -> False

from string import ascii_lowercase


def is_pangram(s: str) -> bool:
    return ''.join(sorted(list(set(i.lower() for i in s.lower() if i in ascii_lowercase)))) == ascii_lowercase
    
print(is_pangram('not pangram'))
