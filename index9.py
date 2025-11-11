# ООП - объектно-ориентированное программирование
# Наследование 
# Инкапсулация
# Полиморфизм
# Абстракция
class Cat: #название класса
    def __init__(self, name, age): # конструктор класса
# магические метод init через два нижних подчеркивания с начала и в конце, обязательно внутри скобок self
        self.name = name # атрибуты класса
        self.age = age # атрибуты класса
    
    def info(self):
        return f"{self.name} {self.age}"
    
cat1 = Cat('Felix', 2) # создание экземпляра / экземпляр класса
# print(cat1.info())
########################
car1_brand = 'Toyota'
car1_year = 2020
car2_brand = 'Kia'
car2_year = 2018

def start_car(brand, year):
    print(car1_brand, car1_year)
    print(car2_brand, car2_year)
###### ООП пример
class Car:
    def __init__(self, brand, year, speed):
        self.brand = brand
        self.year = year
        self.speed = speed
        self.is_going = False

    def re_brand(self, newname):
        self.brand = newname
        return self.brand
    
    def re_year(self, newyear):
        self.year = newyear
        return self.year
    
    def car_is_start(self, kmH):
        self.speed += kmH
        self.is_going = True
 
    def car_is_stop(self):
        self.speed = 0
        self.is_going = False

    def info(self):
        print(f"Бренд: {self.brand} Год: {self.year} Скорость: {self.speed}kmH, Идет: {self.is_going}")

car1 = Car('BMW',2022, 0) # экземпляр класса
car2 = Car('Kia k5',2020, 0) # экземпляр класса
car3 = Car('Mercedes-Benz',2021, 0) # экземпляр класса
car3.info()
car3.re_brand('Matiz')
car3.re_year(2016)
car3.info()