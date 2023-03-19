# Задача №17. Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6


new_list = []
elements_list = int(input('Введите сколько будет элементов в списке '))
element_count = 1
for _ in range(elements_list):                                                # Список заполняется пользователем
    new_list.append(int(input(f'Введите элемент {element_count}: ')))
    element_count = element_count + 1
print(new_list)

new_set = set(new_list) # Создаем из списка множества используя функцию "set"

print(f'Различных чисел в этом списке {len(new_set)}')   # С помощью функции "len" узнаем колличество элементов(длину) множества



