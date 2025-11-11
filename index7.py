# Новая тема: Работа с файлами
# mode - режим:
# r - read - чтение
# w - write - писать - создание нового файла, старый очищает
# a - append - добавлять 
# x - создание нового файла, но если есть такая то вызов ошибка
# b - binary - используется вместе с rb и wb
# t - текстовый режим по умолчанию
# open() функция во круг которого все крутится
# file = open("имя_фамилия", "режим")

# with open('data.txt', 'w', encoding='utf-8') as file:
#     file.write('сегодня ПКС-2-24 сидят на уроке\n')
#     file.write('Марсель сегодня тихий\n')

# with open('sab.txt', 'r', encoding='utf-8') as file:
#     print(file.read())

# with open('sab.txt', 'a', encoding='utf-8') as file:
#     file.write('\nГена программист')

# while True:
#     print(""""
#           1. Лобавляет заметку в файл
#           2. Показывает все заметки
#           3. Ищет заметку по слову
#           4. Заканчивает работу по выбору пользователя""")
#     choice = input("Выберите действие: ")
#     if choice == '1':
#         textUser = input("Что хотите добавить?")
#         with open('bloknot.txt', 'w', encoding='utf-8') as file:
#             file.write(f"{textUser}\n")
#     elif choice == '2':
#         with open('bloknot.txt', 'r', encoding='utf-8') as file:
#             print(file.read())
#     elif choice == '3':
#         textUser = input("Что ищете?")
#         with open('bloknot.txt', 'r', encoding='utf-8') as file:
#             for line in file:
#                 if textUser.lower() in line.lower():
#                     print("Найдено,", line.strip())
#                 else:
#                     print("нет такой заметки")
#     elif choice == '4':
#         break
#     else:
#         print("Выберите от 1го до 4х")
#         continue
# Задача: "Учёт заказов ресторана"
# Условие: Напиши программу, которая:
# 1. Добавляет заказ (блюдо, количество, цена) 
# 2. Показывает все заказы
# 3. Ищет заказы по названию блюда 
# 4. Подсчитывает общую выручку
# 5. Завершает работу по выбору пользователя
while True:
    print("""
        1. Добавляет заказ (блюда, количество, цена)
        2. Показывать все заказы
        3. Ищет заказ по названию блюда
        4. Подсчитывает общую сумму заказа
        5. Заканчивает работу по выбору пользователя""")
    choice = input("Выберите действие: ")
    if choice == '1':
        dish = input("Введите название блюда: ")
        quantity = input("Введите количество: ")
        price = input("Введите цену за единицу: ")
        with open('orders.txt', 'a', encoding='utf-8') as file:
            file.write(f"{dish},{quantity},{price}\n")
    elif choice == '2':
        with open('orders.txt', 'r', encoding='utf-8') as file:
            print(file.read())  
    elif choice == '3':
        search_dish = input("Введите название блюда для поиска: ")
        with open('orders.txt', 'r', encoding='utf-8') as file:
            orders = file.readlines()
            found = False
            for order in orders:
                if search_dish in order:
                    print(order.strip())
                    found = True
            if not found:
                print("Совпадений не найдено")
    elif choice == '4':
        total = 0
        with open('orders.txt', 'r', encoding='utf-8') as file:
            orders = file.readlines()
            for order in orders:
                try:
                    dish, quantity, price = order.strip().split(',')
                    total += int(quantity) * float(price)
                except ValueError:
                    print(f"Ошибка в строке: {order.strip()}")
        print(f"Общая сумма заказа: {total}")
    elif choice == '5':
        print("Работа завершена")
        break   
    else:        
        print("выбирайте от 1 до 5")
        continue
