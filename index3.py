# Задача список любимых фильмов
# У нас есть список фильмов. Студент может добавить фильм, найти фильм в списке или удалить фильм, и наконец фильм.
movies = ("Люси", "Аватар", "Титаник", "Матрица", "Гладиатор")
print('Любимые фильмы', movies)
request = int(input("Нажмите на 1 - если хотите добавить новый фильм.\nНажмите на 2 - если хотите найти фильм.\nНажмите на 3 - если хотите удалить фильм."))
if request == 1:
    new_movie = input('Введите фильм для добавление.').title
    movies.append(new_movie)
    print(movies)
    print("Добавлен новый фильм - " + new_movie)
elif request == 2:
    movie = input('Введите фильм для поиска: ').title
    if movie in orders:
        movies.remove(movie)
        print(movie)
    else:ы
        print("Фильм не найден")
elif request == 3:
    movie = input('Введите фильм для удаления: ').title
    if movie in movies:
        movies.remove(movie)
        print(movies)
        print("Фильм" + movies + "удален")
    else:
        print('Фильм не найден')
elif request == 4:
    print(movies)
    movie = input('Какой фильм хотите изменить: ').title
    if movie in movies:
        rename = input('Введите новое название фильма: ')
        movies.remove(movie)
        movies.append(rename)
        print(movies)
    else:
        print('Фильм не найден')
# Задача список заказов
# У нас есть список блюд, и студент может:
# 1 добавить новое блюдо в заказ,
# 2 проверить, есть ли блюдо в заказе,
# 3 удалить блюдо из заказа,
# 4 изменить блюдо из заказа.
# orders = ["Пицца", "Бургер", "Суши", "Салат", "Паста"]