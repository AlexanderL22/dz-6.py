import random

random_nums = [random.randint(1, 100) for _ in range(200)]
print(f'Список пар, где сумма кортежа кратна 5 -> {list(filter(lambda x: (x[0]+x[1])%5==0, enumerate(random_nums)))}')