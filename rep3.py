store = {
    "Хлебобулочные": {"Хлеб": 30, "Булочка": 20},
    "Мясо": {"Курица": 150, "Говядина": 700},
    "Напитки": {"Сок": 100, "Вода": 30}
}
cart = [] # пустая корзина
while True:
    usl = """
    1. Показать все товары по категориям.
    2. Добавить товар в корзину.
    3. Удалить товар из корзины.
    4. Показать корзину (все товары и итоговую сумму).
    5. Найти самый дорогой и дешевый товар в магазине.
    6. Показать количество товаров в магазине.
    7. Выйти."""
    print(usl)
    request = input("Выберите действие: ")
    if request == '1':
        for category, products in store.items():
            print(category,':')
            for product, price in products.items():
                print(f'. {product} - {price}сом')
    elif request == '2':
        for category in store:
            print(category)
        category = input("Выберите категорию: ").title()
        if category in store:
            print("товары в корзине", category)
            for product, price in store[category].items():
                print(f". - {product}: {price}сом")
            product = input("Введите название товара: ").title()
            if product in store[category]:
                cart.append((product, store[category][product]))
                print(cart)
                "print(f"{product} добавлен в корзину)
            else:
                print("нет такого товара")
        else:
            print("нет такой категории")
    elif request == '3':