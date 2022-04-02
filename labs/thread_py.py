#!/usr/bin/env python
# coding: utf-8

from threading import Thread


# В главном потоке ввожу элементы
print('Введите числа с плавающей запятой через пробел. Например: 1.01 2.345 12.13')
num_list: list = []
for el in input().split():
    num_list.append(float(el))

# В потоке 1: Распечатываю лист
def print_list(x):
    print(f"From child thread: {x}. List = {num_list}")

# В потоке 2: Ищу минимум
def func_min(x):
    print(f"From child thread: {x}. Min element = {min(num_list)}")

# В потоке 3: Ищу максимум
def func_max(x):
    print(f"From child thread: {x}. Max element = {max(num_list)}")

# В потоке 4: Ищу наименее удаленный элемент от среднего арифметического
def nearest_from_mean(x):
    nearest: float = num_list[0]
    mean: float = sum(num_list)/len(num_list)
    for i in range(len(num_list)):
        if abs(num_list[i]-mean)<abs(nearest-mean):
            nearest = num_list[i]
    print(f"From child thread: {x}. Mean = {mean}. Nearest = {nearest}")
    
# Определяю потоки, в которых устанавливаю соответствующие функции с передачей аргумента
th1 = Thread(target=print_list, args={1, })
th2 = Thread(target=func_min, args={2, })
th3 = Thread(target=func_max, args={3, })
th4 = Thread(target=nearest_from_mean, args={4, })
threads = [th1, th2, th3, th4]
for th in threads:
    th.start() # Запускаю потоки
    th.join() # указываю одному потоку дождаться завершения другого потока
