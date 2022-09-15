# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

arr = list(map(float, input('Введи вещественные числа: ').split()))
a = int(input('сколько знаков после запятой вывести: '))

def fractional_difference(numbers_list:list) -> int:
    diff = 0
    for i in range(len(arr)):
        arr[i] = round((arr[i] % 1), a)
    diff = max(arr) - min(arr)
    return (diff)
print(arr)
print(f'Разница между максимальным и минимальным значением дробной части элементов равна {fractional_difference(arr)}')




