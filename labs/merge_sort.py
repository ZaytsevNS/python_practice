import random
from datetime import datetime

start_time = datetime.now()
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    middle = len(arr) // 2
    left = merge_sort(arr[:middle])
    right = merge_sort(arr[middle:])
    return merge(left, right)

def merge(left, right):
    result = []
    while len(left) > 0 and len(right) > 0: #пока не пустые
        if left[0] <= right [0]:           #выбор наименьшего элемента из этих частей
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    
    if len(left)>0:      #если в левой что-то осталось
        result += left   #добавляем к результату
    if len(right)>0:
        result += right
    return result

arr = [random.randint(0, 1000) for i in range(1000)]
print ('Исходный массив: \n' ,arr)
print ('\nОтсортированный массив: ', merge_sort(arr))
end_time = datetime.now()
print('\n\nПрошло времени: {}'.format(end_time - start_time)) 