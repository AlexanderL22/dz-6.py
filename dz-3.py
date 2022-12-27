# 3-Сформировать список из N членов последовательности.
# Для N = 5: 1, -3, 9, -27, 81 и т.д.

number_to_work = int(input('Введите число N -> '))
result = list(map(lambda x: (-3)**x, [x for x in range(number_to_work)]))
print(f'Ваше число -> {number_to_work}, Результат -> {result}')