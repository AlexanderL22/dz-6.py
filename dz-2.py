# 2- Найти произведение пар чисел в списке. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

import math

list_to_work= list(map(int,input('Введите числа через пробел -> ').split()))
source = list(map(lambda x: list_to_work[x] * list_to_work[-(x+1)], [x for x in range(math.ceil(len(list_to_work)/2))]))
print(f'Исходный список - > {list_to_work}; Произведение пар чисел -> {source}')