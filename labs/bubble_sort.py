import random
from datetime import datetime

start_time = datetime.now()
def bubble(data):
    changed = True
    while changed:
        changed = False
        for i in range(len(data) - 1):
            if data[i] > data[i+1]:
                data[i], data[i+1] = data[i+1], data[i]
                changed = True
    return data

arr = [random.randint(0, 1000) for i in range(1000)]
print ('Исходный массив: \n' ,arr)
print ('\nОтсортированный массив: ', bubble(arr))
end_time = datetime.now()
print('\n\nПрошло времени: {}'.format(end_time - start_time))