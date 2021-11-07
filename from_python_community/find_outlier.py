# Условие:

# Ваша задача — написать функцию, которая находит особое число из списка. 
# На вход идёт список из целочисленных значений, все они делятся или не делятся на 2, кроме одного. 
# Вам необходимо найти это особое число. Длина такого списка всегда больше трёх.


def find_outlier(my_list):
    count_even, count_odd = [i for i in my_list if not i % 2], [i for i in my_list if i % 2]
    if len(count_even) < len(count_odd):
        return count_even[0]
    else:
        return count_odd[0]

#my_list = [2, 4, 0, 4, 11, 36] # 11
my_list = [160, 3, 19, 11, -21] # 160
print(find_outlier(my_list))
