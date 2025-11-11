def add_students(students):
    name = input("Введите имя: ").title().strip()
    group = input("Введите название группы: ").strip()
    try:
        age = int(input("Введите возраст: "))
    except ValueError:
        print("Введите только цифры")
    if name in students:
        print("Такой уже существует")
        return
    students[name] = {"группа":group, "возраст":age}
    print(f"Студент {name} добавлен")

def add_subject(subjects):
    name = input("Введите название предмета: ").title().strip()
    teacher = input("Введите Имя и Фамилие учителя: ").title().strip()
    if name in subjects:
        print("Такой предмет уже есть")
        return
    subjects[name] = teacher
    print(f"Предмет {name} добавлен. Препод {teacher} добавлен")

def add_mark(students, subjects):
    name = input("Введите Имя студента: ").title().strip()
    if name not in students:
        print("Такого студента нет!")
        return
    subject = input("Введите предмет: ").strip()
    if subject not in subjects:
        print("Такого предмета нет!")
        return
    try:
        mark = int(input("Введите оценку (0-100): "))
    except ValueError:
        print("Пишите только числа")
        return
    if mark < 0 or mark > 100:
        print("Оценка должна быть от 0 до 100")
    students[name]["оценки"][subject] = mark
    print(f"{name} получил {mark} по предмету {subject}")

def show_student_info(students):
    name = input("Введите Имя студента: ").title().strip()
    if name not in students:
        print("Такого студента нет!")
        return
    data = students[name]
    print(f"Инфо о студенте{name}: ")
    print(f"Группа: {data['группа']}")
    print(f"Возраст: {data['возраст']}")
    print(f"Оценки:")
    if not data('оценки'):
        print("Нет оценок")
    else:
        for subj, mark in data['оценки'].items():
            print(f"{subj}: {mark}")
    avg = calculator_average(data['оценки'])
    print(f"Средний балл: {avg}\n")
def calculator_average(marks):
    if not marks:
        mark = 0
    return round(sum(marks.values()) / len(marks))
    # round() функция которая округляет число float
    # sum складывает числа

def show_top_students(students):
    pass
def expel_students(students):
    pass

students = {}
subjects = {}
while True:
    print("""
        1 Регистрация студентов (имя, группа, возраст)
        2 Добавлять предмет(названиея. преподаватель)
        3 Назначение оценку студентам по предметам
        4 Вычислять средний балл каждого студента
        5 Показывать топ-студентов группы
        6 Проверять, кто подлежит отчислению (если средний балл < 50)""")
    choice = int(input("Выберите действие: "))
    if choice == 1:
        add_students(students)
    elif choice == 2:
        add_subject(subjects)
    elif choice == 3:
        add_mark(students, subjects)
    elif choice == 4:
        show_student_info(marks)
    elif choice == 5:
        show_top_students(students)
    elif choice == 6:
        expel_students(students)
    elif choice == 0:
        print("Выберите действие")
        break
    else:
        print("Вводите от 1го до 6ти")