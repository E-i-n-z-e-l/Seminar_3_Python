# Задача №19. Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

new_list = []
elements_list = int(input('Введите сколько будет элементов в списке '))
element_count = 1
for _ in range(elements_list):                                                # Список заполняется пользователем
    new_list.append(int(input(f'Введите элемент {element_count}: ')))
    element_count = element_count + 1
print(new_list)

number_K = int(input('Введите число K '))

while number_K > len(new_list):                        # Уменьшаем число "K" пока она не станет меньше длины массива
    number_K = number_K - len(new_list)

new_list = new_list[-number_K:] + new_list[:-number_K] # используем "-number_K" для того чтобы двигать элементы списка вправо, а не влево. Если минус не поставить, будет двигать влево.
# С помощью этой операции двигаем элементы массива влево. 
print(new_list)