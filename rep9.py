def car_rental(cars, services):
    total = 0
    orders = []
    chosen_services = []
    name = input("Имя: ")
    try:
        passajirs = int(input("Количество пассажиров: "))
    except ValueError:
        print("Пишите только числа !")
        return
    while True:
        for name in cars:
            print(name, end=", ")
        choice = input("Какой тип машины хотите (стоп): ").title()
        if choice == 'стоп':
            break
        if choice not in cars:
            print("Нет такого типа машины")
            continue
        if passajirs > cars[choice]["макс_пассажиров"]:
            print("Слишком много пассажиров для этой машины")
        if cars[choice]['машины'] == 0:
            print("не осталось машин этой категории. Выберите другие")
            continue
        try:
            days = int(input("Количество дней: "))
        except ValueError:
            print("Пишите только числа !")
        if days <= 0:
            print("Количество дней аренды должно быть положительным")
            continue
        print(services)
        service_input = input("Выберите доп. услуги (нет): ")
        if service_input == 'нет':
            print("ОК")
        elif service_input in services:
            chosen_services.append((service_input, services[service_input]))
        else:
            print("Нет такой доп. услуги")

        bc = cars[choice]['цена'] * days
        total += bc
        cars[choice]['машины'] -= 1
        orders.append(f"{choice} ({days} дней) {total}")
        print(f"Вы арендовали {choice} на {days} дней за {total}сом")

cars = {
"Эконом": {"цена": 2000, "машины": 5, "макс_пассажиров": 4},
"Комфорт": {"цена": 3500, "машины": 3, "макс_пассажиров": 5},
"Бизнес": {"цена": 6000, "машины": 2, "макс_пассажиров": 5},
"Внедорожник": {"цена": 8000, "машины": 2, "макс_пассажиров": 7}
}
services = {
"Детское кресло": 500,
"GPS-навигация": 700,
"Страховка": 1500
}

car_rental(cars, services)