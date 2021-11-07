# Условие:

# Ваша задача — написать функцию, которая подсчитывает количество повторяемых элементов. 
# Желательно выполнить задачу без использования сторонних модулей


def dup_count(string: str) -> int:
    string = string.lower()
    return sum([1 for i in  set(string) if string.count(i) > 1])

#string = 'abcde' # 0
#string = 'indivisibility' # 1
string = 'Indivisibilities' # 2
#string = 'aA11' # 2
print(dup_count(string))
