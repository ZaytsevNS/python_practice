# подключаем необходимые библиотеки
from sympy import *
import math


def taylor(y, dy):
    """ Функция подсчета ряда Тейлора. """
    x = symbols("x") # возвращаем ссылку на символьный объект
    target_function = sin(x) # целевая функция -> можно изменить, к примеру на cos(x)
    list_of_functions = [] # список функций
    list_of_functions.append(target_function) # добавляем в список функций целевую функцию

    for i in range(len(list_of_functions) + 1): # цикл по всем элементам в 'list_of_functions'
        list_of_functions[i] = diff(list_of_functions[i - 1]) # находим производные элементов, которые в 'list_of_functions'
        list_of_functions.append(diff(list_of_functions[i])) # добавляем производные в список функций
    print('ПРОИЗВОДНЫЕ: ', list_of_functions, '\n') # выводим на печать производные, которые сейчас в 'list_of_functions'
    for j in range(len(list_of_functions)): # цикл по всем элементам в 'list_of_functions'
        list_of_functions[j] = list_of_functions[j].subs(x, 5).evalf() # высчитываем значения функций, которые в 'list_of_functions', подставляя вместо 'x' -> '5'
    print('ЗНАЧЕНИЯ ФУНКЦИЙ в Х=5: ', list_of_functions, '\n') # выводим на печать значения функций

    value_of_sin5 = [] # инициализируем объект типа list
    value_of_sin5.append(math.sin(y)) # добавляем в list 'value_of_sin5' значение sin(5), которое находится из библиотеки math
    print('ЗНАЧЕНИЕ sin(5) из БИБЛИОТЕКИ math: ', value_of_sin5, '\n') # выводим данное значение на печать

    values_of_row_element = [] # инициализируем объект типа list
    values_of_row_element.append(list_of_functions[0]) # в лист 'values_of_row_element' добавляем значение cos(5) -> f(y)

    for k in range(len(list_of_functions)): # цикл по элементам в листе 'list_of_functions':
        values_of_row_element[k] = list_of_functions[k]*math.pow(dy, k+1) / math.factorial(k+1) # считаем следующие элементы ряда Тейлора: f`(y)*dy+(f``(y)*dy^2)/2+(f```(y)*dy^3)/6
        values_of_row_element.append(values_of_row_element[k]) # добавляем подсчитанные элементы ряда Тейлора в лист 'values_of_row_element'
    print('z1 = ', values_of_row_element[0], 'z2 = ', values_of_row_element[1], 'z3 = ', values_of_row_element[2], '\n')
    print(f'Cумма t0, z1, z2, z3 = {sum(value_of_sin5 + values_of_row_element)}') # распечатаем значение функции sin(y+dy) сложив все элементы ряда Тейлора
    print('Значение sin(y+dy) =  ', math.sin(y+dy)) # распечатаем значение функции sin(y+dy) из библиотеки math
    

taylor(5, 0.01) # начальные условия -> первый параметр - значение 'y', второй параметр - значение 'dy'
