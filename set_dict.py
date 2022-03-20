# Problem 1
# Найти объекты которые есть и в SET №2 и в SET №3 из Google Colab
# # Множество № 2:
# farm_1 = {"dog", "cat", "mouse", "sheep"}

# # Множество № 3:
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}

# farm_1 = {"dog", "cat", "mouse", "sheep"}
# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# total = farm_1.intersection(farm_2)
# print(total)

# Problem 2
# В SET №3 из Google Colab найдите объекты которых нет SET №2

# farm_2 = {"cow", "horse", "donkey", "cat", "dog"}
# farm_1 = {"dog", "cat", "mouse", "sheep"}
#
# total = farm_2.difference(farm_1)
# print(total)


# Problem 3
# Создайте SET из 5 элементов. Потом добавьте в SET ещё один элемент.
# А затем удалите через .pop() элемент и посмотрите что же вы удалили.

# sett = {'a','b','c',1,0}
# total = sett.pop()
# print(sett)
# print(total)


# Problem 000:
# Из Dictionary №1:
# Добавьте в меню
#  'besh_barmak' который стоит  130 сом.
# Оказалось лагман слишком дешевый. Обновите цену на 135
# Ваш повар отвратительно готовит борщ, поэтому хотите удалить это блюдо.
# Удалить borsh

# menu = \
#     {'lagman': 120,
#      'plov': '120',
#      'borsh': 100}
# menu.update(besh_barmak=130, lagman=135)
# del menu['borsh']
# print(menu)


# Problem 10
# Из Dictionary №1
# Добавьте в меню
# напитки как ключ "drinks",
# А список всех доступных напитков: ['Coca-Cola', 'Sprite', 'Fanta'] как его значение.

# menu = \
#     {'lagman': 120,
#      'plov': '120',
#      'borsh': 100}
# drinks = {'drinks':['Coca-Cola', 'Sprite', 'Fanta']}
# menu.update(drinks)
# print(menu)


# Problem 31:
# Создайте пустой словарь.
# Запустите цикл который 3 раза спросит его имя и его пароль.
# Записывайте имя пользователя как ключ, а пароль как его значение.


# count = 1
# db = {}
# while count < 4:
#     get_name = input('name: ')
#     get_password = input('password: ')
#     # db.update(get_name = get_password)
#     db[get_name] = get_password
#     count += 1
# print(db)


# Problem 27:
# Создайте Dictionary с 5 элементами где ключи это их имена, а значение их профессия.
# С помощь цикла for пройти вывести на экран строку:
# "Здравствуйте <Имя>  Прекрасная профессия <Профессия>"

# db = {
#     'asan':'teache',
#     'asan1':'teach',
#     'asan2':'teac',
#     'asan3':'tea',
#     'asan4':'te',
#     }
#
# for key,value in db.items():
#     print(f"Здравствуйте {key}  Прекрасная профессия {value}")


# Problem 22:
# Создайте цикл который справшивает у пользователя 10 чисел и добавьте их в SET.
# Сделайте так чтобы эти данные уже никто не смог поменять позже.

# set = set()
# count = 0
# while count < 10:
#     login = input('введите логин : ')
#     password = input('введите логин : ')
#     set.add(login)
#     set.add(password)
#     count += 1
# print(tuple(set))


# Problem 11:
# Есть список Южноамериканских стран
# СПИСОК №2
# в котором Суринам встречается два раза. Необходимо написать программу,
# которая удалит дублирующуюся запись, и возвратит в результате список.

# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
#   'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
#
# make_set = set(south_american_countries)
# make_list = list(make_set)
# print(make_list)


# Problem 101:
# Вы собираетесь на Иссык-Куль. Пока ваш чемодан пуст:
# suitcase = []
# Однако он
# может вместить всего 5 вещей.
# Положите 5 вещей в чемодан.
# Вы передумали, и решили убрать последнюю вещь.

# suitcase = []
# count = 0
# while count < 5:
#     suitcase.append('hat')
#     count += 1
# print(suitcase)
# dell = suitcase.pop(4)
# print(suitcase)