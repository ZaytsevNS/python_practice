# Узнать расширение файла по его имени. Иначе пустую строку

# file -> ''
# .not_ext. -> ''
# file.py.exe -> exe
# script.py -> py

def format(s: str) → str:
    split_str: list = s.split('.')
    return split_str[-1] if len(split_str[-1]) != 0 and len(split_str) > 1 else ''
