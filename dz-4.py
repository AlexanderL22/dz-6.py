# 4 - Дан список URL различных сайтов. Нужно составить список доменных имен сайтов.

URL_list = ['https://city.Hello-Kitty-Home.com/hello/','https://МРЭСК.рф/Приветствие/','https://www.NFS3DTHS.ru/','https://Bolschoy-voprosnik.su/vopros/kak-dela/']
result = list(map(lambda x: URL_list[x].partition('//')[-1],[x for x in range(len(URL_list))]))
result = list(map(lambda x: result[x].partition('/')[0],[x for x in range(len(result))]))
print(f'Исходный список {URL_list} ; результат -> {result}')