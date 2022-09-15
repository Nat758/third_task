# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = int(input('Введи число: '))

def decimal_to_binary (number) ->int:
    binary = ''
    while number > 0:
        binary = str(number % 2) + binary
        number = number // 2
    return binary
print(decimal_to_binary(number))