# Теория

# any = 7
# print(id(any)) # Показывает какой id занимает в памяти компьютера этот элемент


# import time
#
# some_list = [random.randint(1, 1000000) for _ in range(1000000)]
#
# start = time.perf_counter()
# print(100234 in some_list)
# end = time.perf_counter()
# first_time = end - start
#
# some_set = set(some_list)
#
# start = time.perf_counter()
# print(40 in some_set)
# end = time.perf_counter()
# second_time = end - start
# print(first_time / second_time)


# Словари

some_dict = {'name': 'Alex', 'surname': 'Salnikov'}
print(some_dict.get('address', 'Такого ключа нет'))     # для того чтобы программа продолжала работать не взирая на то, что в словари нет искомого ключа


print(some_dict.values()) # Посмотреть все значения в словаре
print(some_dict.keys())   # Посмотреть все ключи в словаре