import random
from datetime import datetime

start_time = datetime.now()
def quicksortBetter(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quicksortBetter(left) + middle + quicksortBetter(right)

arr = [random.randint(0, 100000) for i in range(100000)]
print ('Исходный массив: \n' ,arr)
print ('\nОтсортированный массив: ', quicksortBetter(arr))
end_time = datetime.now()
print('\n\nПрошло времени: {}'.format(end_time - start_time))