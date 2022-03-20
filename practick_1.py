# 1(Множества)


# 1.Объединить 2 множества
# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
# 2.Добавить месяц, которого нету во множестве
# 3.Перебрать элементы множества
# 4.Вам даны 2 множества, узнать какие элементы пересекаются между ними.
# x = {1, 2, 3}
# y = {4, 3, 6}


# months_a = set(["Jan", "Feb", "March", "Apr", "May", "June"])
# months_b = set(["July", "Aug", "Sep", "Oct", "Nov"])
# months_b.add('Dec')

# #2 print(months_b)

# #1 a = months_a.union(months_b)
# print(a)
#
# #3
# for i in a:
#     print(i)

   #4
# x = {1, 2, 3}
# y = {4, 3, 6}
# c = x.intersection(y)
# print(c)


# 2(Словари)
# Написать скрипт который проходится по ключам и проверяет значения
# a) Если значение делиться на 3, то записываем строку “Hi”
# b) Если значение делиться на 5, то записываем строку “Bye”

# ПРИМЕР:
# Дано -> dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# Результат -> a = Bye
# b = Hi

# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 14}
# for key in dict1:
#     if dict1[key] % 5 == 0:
#         dict1[key] = 'Bye'
#     elif dict1[key] % 3 == 0:
#         dict1[key] = 'Hi'
#     else:
#         dict1[key] = 'error'
# print(dict1)

    #3

# Напишите программу для слияния нескольких словарей в один.


# my_friends = {
#     "Joomart": "+996555246810",
#     "Adinai": "+996555013579",
#     "Ermek": "+996777013579",
#     "Atai": "+996777246810",
#     "Aslan": "+996999246810"
#  }
#
# his_her_friends = {
#     "Lyazat": "+996551123456",
#     "Salavat": "+996552234567",
#     "Daniyar": "+996553345678",
#     "Bolot": "+996554456789",
#     "Alymbek": "+996555501234",
#     "Dastan": "+996556678912",
#     "Maksat": "+996557789012",
#     "Aibek": "+996558890123"
#  }
#
# # my_friends.update(his_her_friends)
# # print(my_friends)
#
# our_friends = {**my_friends,**his_her_friends}
# print(our_friends)

