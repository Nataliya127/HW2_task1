# 1'. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# *Пример:*

# - 6782 -> 23
# - 0,56 -> 11

num = input('Введите число: ' ' ')
n_sum = 0
def n_sum(num):
    return sum(map(int, num.replace('.', '').replace('-', ' ')))

print(f'Сумма цифр в числе: {n_sum(num)}')

