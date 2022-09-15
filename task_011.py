# Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

array = list(map(int, input('Введи числа: ').split()))

def product_of_pairs(numbers_list:list) -> list:
    result_list = []
    first_index = 0
    last_index = len(numbers_list) - 1
    while last_index - first_index >= 0:
        result_list.append(numbers_list[first_index] * numbers_list[last_index])
        first_index += 1
        last_index -= 1
    return result_list
print(f'Исходный массив: {array}')
print(f'Массив из произведений пар исходного массива {product_of_pairs(array)}')
         

