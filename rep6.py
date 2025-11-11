usl = """
1. Показать всех учеников и оценки.
2. Добавить ученика.
3. Добавить предмет ученику.
4. Добавить оценку по предмету ученика.
5. Показать все предметы и оценки ученика.
6. Посчитать среднюю оценку ученика.
7. Посчитать общую среднюю оценку по всему классу.
8. Выйти."""
students = {
"Нурислам": {
"Математика": [5, 4],
"История": [3, 4]
},
"Арген": {
"Физика": [4, 5],
"Литература": [5]
}
}
print(usl)
while True:
    req = input("Введите действие: ")
    if req == '1':
    for name, predmets in students.items():
    print(name)
    for pred, bal in predmets.items():
    print(f" {pred}: {bal}")
    elif req == '2':
    name = input("Добавить ученика: ")
    students[name] = {}
    print("Добавлен в наш список")
    elif req == '3':
    name = input("К какому ученику добавить предмет: ")
    predmet = input("Добавить предмет ученику: ")
    students[name][predmet] = []
    print("Успех")
    elif req =='4':
    name = input("К какому ученику добавить оценку: ")
    if name in students:
    predmet = input("Выбрать какому предмету: ")
    if predmet in students[name]:
    ball = int(input("Добавить оценку: "))
    students[name][predmet].append(ball)
    print("Успех")
    else:
    print("нет такого предмета. Выберите 3 и добавьте предмет")
    else:
    print("Нет такого ученика")