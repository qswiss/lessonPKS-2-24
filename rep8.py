def number_larger():
    a = int(input("Введите число: "))
    b = int(input("Введите второе число: "))
    if a or b < 0:
        pol_chisl1 = abs(a)
        pol_chisl2 = abs(b)
        if pol_chisl1 > pol_chisl2:
            print(pol_chisl1)
        else:
            print(pol_chisl2)
    else:
        print("Ошибка")

def number_equal():
    a = int(input("Введите число: "))
    b = int(input("Введите второе число: "))
    if a == b:
        print("Yes")
    else:
        print("No")

def bolshesto():
    a = int(input("Введите число: "))
    if a > 100 or a < -100:
        print("---")
    else:
        print("+")

def month():
    month = int(input("Введите номер месяца: "))
    if month == 12 or month == 1 or month ==2:
        print("Зима")
    elif month == 3 or month == 4 or month == 5:
        print("Весна")
    elif month == 6 or month == 7 or month == 8:
        print("Лето")
    elif month == 9 or month == 10 or month == 11:
        print("Осень")

def three_numbers():
    a = int(input("Введите число: "))
    b = int(input("Введите второе число: "))
    c = int(input("Введите третье число: "))
    summa = sum(a, b, c)
    if summa > 18:
        print("Yes")
    else:
        print("No")

def first_numberhz():
    first_num = int(input("Введите число: "))
    if first_num % 3 == first_num % 5 == 0:
        print("Ого, делится")
    elif first_num % 3 == 0:
        print("Арара")
    elif first_num % 5 == 0:
        print("Огого")
    else:
        print("kill yourself")

def albert():
    age = int(input("Введите возраст: "))
    if age < 18:
        print("Рано")
    elif age >= 18 and age <= 40:
        print("Идем служить")
    elif age > 40:
        print("Уже не надо")

print(albert())