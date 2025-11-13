# Декораторы добавяют функциональность в существующий код
# Декоратор - это паттерн програмирования, который позвляет добавлять новый функционал к нашей сущ.функции
# Функция = это объект
def great():
    print("Привет")

hello = great
hello()
##########
def shout(text):
    return text.upper()

def whisper(text):
    return text.lower()

def speak(func):
    message = func('Hello PKS-2-24')
    print(message)

speak(shout)
speak(whisper)


################

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def operate(func, x):
    result = func(x)
    return result

print(operate(inc, 6))
print(operate(dec, 8))
###########
def oute():
    def inner():
        print("Я функция внутри")
    return inner
# oute - возвращает другую функци.
newFunc()
##########
def before_after(func):
    def wrapper():
        print("Перед вызовом")
        func()
        print("После вызова")
    return wrapper

@before_after # декоратор
def say_hi():
    print("Привет друг")

say_hi()
############

def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Вызов функции {func.__name__} с аргументами {args} {kwargs}")
        result = func(*args, **kwargs)
        print(f"Результат: {result}")
        return result
    return wrapper

@logger
def add(*args, **kwargs):
    return sum(args) + sum(kwargs.values())

add(5,10,5)
add(a=5 b=8)
#############
# @property - это встроенный декоратор
# позволяет нам обращаться к методу как в обычному полю атрибута
# без @property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    def get_area(self):
        return 3.14 * self._radius**2
    
c = Circle(5)
print(c.get_area)

# с декоратором @property
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def area(self):
        return 3.14 * self._radius**2
    
c = Circle(5)
print(c.area)
###############
class Person:
    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        print("Сеттер сработал")
        if not isinstance(value, str): # проверяет не явл ди value стр
            raise ValueError("Имя должно быть строкой")
        self._name = value

p = Person('Gena')
p.name = 'Alez'
print(p.name)
del p.name