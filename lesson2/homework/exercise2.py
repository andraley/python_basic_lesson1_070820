"""2. Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input().
"""

#Объявление списка в который пользователь будет записывать даные
user_list = []

#Циклы для записи данных в список
while True:
    object = input('Введите новый объект в список. Для прекращения напишите exit.\n')
    if object == 'exit': #Условие для прекращения записи в цикл
        break
    user_list.append(object)

"""""Объявления переменой для итерации цикла
и нового списка куда будут записываться перевернутые данные
"""
i = 0
new_list = []

#Цикл для переворачивания данных
while i < len(user_list):

    a = user_list[i]
    i += 1
    if i == len(user_list): #Выход из цикла в случае если длинна нечетная
        new_list.append(a)  #Последный объек записывется на тоже место
        break
    b = user_list[i]
    i += 1
    new_list.append(b)
    new_list.append(a)

#Вывод полученых списков
print(f"Список который вы ввели: {user_list}")
print(f"Перевернутый список: {new_list}")


