# Задача: Система авиабронирования
# Создай программу, используй классы, инкапсуляцию и взаимодействие объектов.
# Программа должна позволять: добавлять и удалять рейсы, покупать и отменять билеты, изменять параметры рейса, рассчитывать общую выручку, показывать статистику.

# Класс Flight: Отвечает за конкретный рейс. Содержит: направление (route), количество мест эконом и бизнес, цены, количество проданных билетов, методы для продажи, отмены и изменения данных.

# Класс Airline: Управляет всеми рейсами: список (или словарь) всех рейсов, методы добавления, удаления, поиска и статистики. 

# Класс Client: Сохраняет данные клиента и купленного билета.

from typing import List

class Flight:
    """Класс, представляющий авиарейс."""
    def __init__(self, flight_number: str, origin: str, destination: str, price: float, seats: int):
        self.__flight_number = flight_number
        self.__origin = origin
        self.__destination = destination
        self.__price = price
        self.__seats = seats
        self.__sold_tickets = 0

    # Геттеры и сеттеры (инкапсуляция)
    @property
    def flight_number(self):
        return self.__flight_number

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price: float):
        if new_price > 0:
            self.__price = new_price

    @property
    def available_seats(self):
        return self.__seats - self.__sold_tickets

    def buy_ticket(self, quantity: int = 1):
        """Покупка билета(ов)."""
        if quantity <= self.available_seats:
            self.__sold_tickets += quantity
            print(f"Куплено {quantity} билет(ов) на рейс {self.__flight_number}")
        else:
            print(f"Недостаточно мест! Осталось {self.available_seats}")

    def cancel_ticket(self, quantity: int = 1):
        """Отмена билета(ов)."""
        if quantity <= self.__sold_tickets:
            self.__sold_tickets -= quantity
            print(f"Отменено {quantity} билет(ов) на рейс {self.__flight_number}")
        else:
            print("Ошибка: нельзя отменить больше билетов, чем куплено.")

    def total_revenue(self):
        """Общая выручка по рейсу."""
        return self.__sold_tickets * self.__price

    def __str__(self):
        return (f"Рейс {self.__flight_number}: {self.__origin} ✈ {self.__destination}, "
                f"Цена: {self.__price}₽, Свободных мест: {self.available_seats}")


class AirlineSystem:
    """Класс для управления авиарейсами."""
    def __init__(self):
        self.__flights: List[Flight] = []

    def add_flight(self, flight: Flight):
        self.__flights.append(flight)
        print(f"Добавлен рейс {flight.flight_number}")

    def remove_flight(self, flight_number: str):
        for f in self.__flights:
            if f.flight_number == flight_number:
                self.__flights.remove(f)
                print(f" Рейс {flight_number} удален")
                return
        print(f"Рейс {flight_number} не найден")

    def find_flight(self, flight_number: str) -> Flight:
        for f in self.__flights:
            if f.flight_number == flight_number:
                return f
        print(f"Рейс {flight_number} не найден")
        return None

    def total_revenue(self):
        """Общая выручка по всем рейсам."""
        return sum(f.total_revenue() for f in self.__flights)

    def show_statistics(self):
        """Показать статистику по всем рейсам."""
        print("\n Статистика авиарейсов:")
        for f in self.__flights:
            print(f"{f} | Выручка: {f.total_revenue()}₽")
        print(f"\n Общая выручка: {self.total_revenue()}₽\n")


# ======== Пример использования ========

if __name__ == "__main__":
    system = AirlineSystem()

    # Добавляем рейсы
    f1 = Flight("SU123", "Москва", "Сочи", 7500, 150)
    f2 = Flight("UT456", "Санкт-Петербург", "Казань", 6500, 100)
    f3 = Flight("AF789", "Москва", "Париж", 25000, 200)

    system.add_flight(f1)
    system.add_flight(f2)
    system.add_flight(f3)

    # Покупаем и отменяем билеты
    f1.buy_ticket(3)
    f2.buy_ticket(2)
    f3.buy_ticket(5)
    f3.cancel_ticket(2)

    # Изменяем цену
    f2.price = 7000

    # Удаляем рейс
    system.remove_flight("UT456")

    # Показываем статистику
    system.show_statistics()