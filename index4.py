def fitnes_centr(plans, services):
    total = 0
    orders = []
    name = input("Ваше имя: ").title().strip()
    if name in clients:
        print(f"С возвращением, {name}")
        level = clients[name]['уровень']
        points = clients[name]['баллы']
    else:
        print("Добро пожаловать в фитнес зал!")
        level = input("Ваш уровень для тренировок[начальный / средний / продвинутый]: ")
        clients[name] = {'уровень': level, "баллы": 0, "история": []}
        points = 0
    level_rank = {'начальный': 1, 'средний': 2, 'продвинутый': 3}
    if level not in level_rank:
        print("Ошибка: неверный уровень: ")
        return
    
    while True:
        print("Доступные абонементы: ")
        for plan, info in plans.items():
            print(plan, info)
        choice = input("Выберите абонемент (или 'стоп'): ").title().strip()
        if choice == "Стоп":
            break
        if choice not in plans:
            print("Такого абонемента нет.")
            continue
        if plans[choice]["места"] == 0:
            print("Мест не осталось")
            continue
        if level_rank[level] < level_rank[plans[choice]['уровень']]:
            print("Ваш уровень недостаточен для этого абонемента")
            continue
        try:
            count = int(input("Количество абонементов хотите? "))
        except ValueError:
            print("Пишите только числа")
            continue
        if count > plans[choice]["места"]:
            print("Недостаточно мест, у нас только этот тариф: ", plans[choice]["места"])
            continue

        choice_service = input(f"Доп.услуги: {', '.join(services.keys())} или 'нет':").split(', ')



plans = {
    "Месячный": {"цена": 10000, "места": 10, "уровень": "начальный", "тренировок": 12},
    "Полугодовой": {"цена": 45000, "места": 5, "уровень": "средний", "тренировок": 72},
    "Годовой": {"цена": 80000, "места": 3, "уровень": "продвинутый", "тренировок": 150}
}
services = {
    "Тренер": 5000,
    "Питание": 3000,
    "Бассейн": 4000
}
clients = {}

fitnes_centr(plans, services)