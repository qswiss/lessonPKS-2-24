listPass = {'Gena': 'qwerty'}
login = input("Введите логин: ")
if login in listPass:
    attempts = 3
    while attempts > 0:
        password = input("Введите пароль: ")
        if password  == listPass[login]:
            print("Вы успешно вошли в систему")
            break
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Неверный пароль! Осталось попыток: {attempts}")
            else:
                print("Вы превысили лимит попыток. Попробуйте снова через 5 минут.")
else:
    print("Пользователь не найден.")