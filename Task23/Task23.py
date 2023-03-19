# Задача №23. Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером) 
# Пример:
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)

new_list = []
elements_list = int(input('Введите сколько будет элементов в списке '))
element_count = 1
for _ in range(elements_list):                                                
    new_list.append(int(input(f'Введите элемент {element_count}: ')))
    element_count = element_count + 1
print(new_list)

count = 0
for i in range(elements_list - 1):
    if new_list[i] < new_list[i + 1]:
        count = count + 1
print(count)





















