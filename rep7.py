def car_rental(cars, services):
    name = input("Введите ваше имя: ")
    try:
        passengers = int(input("Введите количество пассажиров: "))
    except ValueError:
        print("Введите целое число для количества пассажиров.")
        return
    orders = []
    total_price = 0
    while True:
        choice = input("\nВыберите категорию машины (или введите 'стоп' для завершения): ").capitalize()
        if choice.lower() == 'стоп':
            break
        if choice not in cars:
            print("Такой категории нет. Повторите ввод.")
            continue
        car_info = cars[choice]
        if car_info['машины'] == 0:
            print("Извините, в этой категории нет доступных машин.")
            continue
        if passengers > car_info['макс_пассажиров']:
            print(f"Выбранная категория поддерживает максимум {car_info['макс_пассажиров']} пассажиров.")
            continue
        try:
            days = int(input("Введите количество дней аренды: "))
            if days <= 0:
                print("Количество дней должно быть положительным.")
                continue
        except ValueError:
            print("Введите целое число.")
            continue
        extra_services_input = input("Введите дополнительные услуги через запятую (или оставьте пустым): ").strip()
        selected_services = []
        services_price = 0
        if extra_services_input:
            for service in extra_services_input.split(','):
                service = service.strip()
                if service in services:
                    selected_services.append(service)
                    services_price += services[service] * days
                else:
                    print(f"Услуга '{service}' не найдена и будет проигнорирована.")
        base_price = car_info['цена'] * days
        total_order_price = base_price + services_price
        orders.append({
            "категория": choice,
            "дни": days,
            "услуги": selected_services,
            "цена": total_order_price
        })
        total_price += total_order_price
        cars[choice]['машины'] -= 1
        print(f"Машина категории '{choice}' успешно арендована на {days} дней. Сумма: {total_order_price} сом.")
    discount = 0
    if total_price > 25000:
        discount = total_price * 0.1
        total_price -= discount

    print("\n=== ИТОГОВАЯ ИНФОРМАЦИЯ ===")
    print(f"Арендованные машины для {name}:")
    for i, order in enumerate(orders, 1):
        print(f"{i}. Категория: {order['категория']}, Дней: {order['дни']}, Услуги: {', '.join(order['услуги']) or 'Нет'}, Сумма: {order['цена']} сом")
    if discount:
        print(f"\nБыла применена скидка 10%: -{int(discount)} сом")
    print(f"\nИтоговая сумма к оплате: {int(total_price)} сом")
    print("\nОставшиеся машины по категориям:")
    for cat, info in cars.items():
        print(f"{cat}: {info['машины']} машин(ы)")

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
