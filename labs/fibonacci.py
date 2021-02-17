fib_results = {0:0, 1:1}
def fibfunc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        value_fib = fibfunc(n-1) + fibfunc(n-2)
        fib_results[n]=value_fib
        return value_fib

n_fib = int (input ('Введите количество чисел последовательности Фибоначчи: '))
v_fib = fibfunc(n_fib)
print ('\n{}-й элемент ряда Фибоначчи = {}'.format(n_fib, v_fib))
print ('\nПоследовательность Фибоначчи: \n',fib_results.values())