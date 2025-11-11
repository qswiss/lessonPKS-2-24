# print("hello"*100)
# print("hello")
# print("hello")
# print("hello")

# циклы: for-для and while-пока

# цикл for нужен чтобы повторять действие несколько раз, (список, строка, диапоз чисел, кортежи и т.д.)

# цикл - это когда программа повторяет одно и то же действие много раз

# цикл for перебирает элементы какого-то набора (списка, строки, диапазона чисел и т.л.)

# range() "генератор чисел", он создает последовательность чисел которые удобно перебирать в цикле

# for - переменная in последовательность:
#   действие

# range(start,stop,step) - генератор чисел, он создает последовательность чисел по которой проходит цикл

# for num in range(0, 101, 2):
#     print(num,'hello')

# names = ['jiraf', 'Aibek', 'begemot', 'Gena', 'begemot', 'Gena', 'Mars']
# for itemkey, value in names_age.items():
#     print(itemkey, value)

# for num in range(0, 101, 2):
#     print(num,'hello')

# numbers = []
# for num in range(1,101,2):
#     numbers.append(num)
# print(numbers)

# name = 'Abdul345bosid35'
# nums = []
# for n in name:
#     if n.isdigit():
#         nums.append(n)
# print(nums)

# lista = ['Gena', 'Aibek', 'Mili']
# lst = []
# for l in lista:
#     lst.append(l.upper())
# print(lst)

# float
# str
# int
# bool
# list [] изменяемый тип данных
# tuple () неизменяемый тип данных
# set - множества - {34,46,557)
# dict - dictionary - словари {key:value}
# names = {
#     'Elnura': 18,
#     'Davlet': 24,
#     'Gena': 34,
# }
# for n, v in names.items():
#     print(n, v+1)

# у нас есть список телефонных номеров, нам надо создать программу которая будет спрашивать действие:
# 1 - добавить новый номер телефона
# 2 - удалить номер телефона
# 3 - поиск имени и вывод имени и телефона
# 4 - изменение имени и телефона
# также должна быть проверка на длину имени, имя должен быть выше двух символов
# номер телефона должен быть ровно из 9 символов, не больше и не меньше, программа должна проверять это и если не соответсвует длине, то говорить пользователю о том что надо исправить
# contact_names = {
#     'Davlet': 770700700,
#     'Aliya': 202456456,
#     'Adilet': 550343434,
# }
# print('Ваши контакты', contact_names)
# num_request = input("1 - добавить новый номер телефона\n2 - удалить номер телефон\n3 - поиск имени и вывод имени и телефона\n4 - изменение имени и телефона\nВыберите действие: ")
# if num_request == '1':
#     new_name = input("Введите имя: ")
#     if len(new_name) > 2 and len(new_name)< 20:
#         new_numbers = input("Введите номер телефона: ")
#         if len(new_numbers) == 9:
#             contact_names[new_name] = new_numbers
#             print(contact_names)
# #     else:
#         print("имя должно быть от 3х и выше смволов")
# elif num_request == '2':
#     for i, v in contact_names.items():
#         print('Имя:', i, "Номер:",v)
#     del_name = input("Введите имя для удаления: ").title()
#     if del_name in contact_names.keys():
#         print(contact_names[del_name], 'успешно удален')
#         del contact_names[del_name]
#         print(contact_names)
#     else:
#         print(del_name, 'не найден')
# elif num_request == '3':
#     search_name = input("Введите имя для поиска: ").title()
#     if search_name in contact_names.keys():
#         print(search_name, contact_names[search_name])
#     else:
        
#             contact_names[new_name]=contact_names.pop(old_name)
#             print("Контак успешно изменен")
#             print(contact_names)
# elif choice == '2':
#     name = input('Введите имя контакьа:').title()
#     if name in contact_names.keys():
#         new_phone = input('Введите номер:')
#         if len(new_phone) == 9:
#                 contact_names[name]= new_phone
#                 print("Успешно изменено")
#                 print(contact_names)
#         else:
#                 print("Длина номера от 9 символов")
#     else:
#             print("Нет такого контакта")


# В ресторане есть меню блюд и меня напитков.
# Программа в цикле while показывает меню действий:
# 1. Показать меню блюд
# 2. Показать меню напитков.
# 3. Заказать блюдо
# 4. Заказать напиток
# 5. Показать корзину и итоговую сумму
# 6. Выйти
# Так пользователь сможет заказывать несколько раз и считать общую сумму.
# Меню ресторана 
menu_food = {
     'Плов': 250,
     'Манты': 300,
     'Лагман': 280,
     'Шашлык': 400,
     'Бешбармак': 500
}
menu_drinks = {
     'Чай':50,
     'Кофе': 120,
     'Кумыс': 150,
     'Айран': 80,
     'Сок': 100
}
cart = [] # Ваша корзина куда кладется стоимость заказов
while True:
    req = int(input('1. Показать меню блюд\n2. Показать меню напитков\n3. Заказать блюдо\n4. Заказать напиток\n5. Показать корзину и итоговую сумму\n6. Выйти\nВыберите действие:'))
    if req == 1:
        for k,v in menu_food.items():
            print(f"{k}: {v}сом")
    elif req == 2:
        for k,v in menu_drinks.items():
            print(f"{k}: {v}сом")
    elif req == 3:
        print(menu_food)
        name_food = input("какое блюдо хотите?:").title()
        if name_food in menu_food:
            cart.append(menu_food[name_food])
            print(cart)
        else:
            print("Такое блюдо не найдено !")     
    elif req == 4:
        print(menu_drinks)
        name_drinks = input("какой напиток хотите?:").title()
        if name_drinks in menu_drinks:
            cart.append(menu_drinks[name_drinks])
            print(cart)
        else:
            print("Такой напиток не найден !")
    elif req == 5:
        if cart:
            print("В корзине", len(cart))
            total = sum(cart)
            print("Общая сумма:", total)
        else:
            print("Вы ничего не заказали")
    elif req == 6:
        print("Спасибо что посетили")
        break
    else:
        print('Неверный выбор ! Выберите от 1 до 6')