# Условие:
# Дано два списка, вам нужно проверить, являются ли элементы внутри первого списка квадратом элементов из второго списка. Порядок не имеет значения.

def same(list1: list, list2: list) -> bool:
    return sorted([i**2 for i in list1]) == sorted(list2) if len(list1) == len(list2) else False
  
