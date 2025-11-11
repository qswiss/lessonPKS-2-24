class Transport:
    def __init__(self, speed, capacity):
        self._speed = speed
        self._capacity = capacity

    def start(self): # сообщает что транспорт начал движение
        print("Транспорт начал движение")
    def stop(self): # сообщает что транспорт остановил движение
        print("Транспорт остановился")
    def info(self): # сообщает что транспорт начал движение
        print(f"Скорость: {self._speed} км/ч")
        print(f"Вместимость: {self._capacity} пассажиров")
    
class Car(Transport):
    def __init__(self, speed, capacity, brand):
        super().__init__(speed, capacity)
        self.brand = brand 

    def info(self):
        base_info = super().info()
        print(f"Автомобиль {self.brand}: {base_info}")

class Bus(Transport):
    def __init__(self, speed, capacity, route_number):
        super().__init__(speed, capacity)
        self.route_number = route_number 

    def info(self):
        base_info = super().info()
        print(f"Автобус {self.route_number}: {base_info}")

class Electric:
    def __init__(self, battery_level):
        self._battery_level = battery_level

    def charge(self):
        self._battery_level = 100
        print("Батарея полностью заряжена")

    def battery_status(self):
        print(f"Уровень заряда батареи: {self._battery_level}%")

class ElectricCar(Car, Electric):
    def __init__(self, speed, capacity, brand, battery_level=100):
        Car.__init__(self, speed, capacity, brand)
        Electric.__init__(self, battery_level)

    def info(self):
        super().info()
        print(f"Уровень заряда батареи: {self._battery_level}%")