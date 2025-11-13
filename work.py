class Tour:
    def __init__(self, id, price, days):
        self.__id = id
        self.__price = None #приватный атрибут price
        self.price = price #установленный setter
        self._is_booked = False
        self._client = None
        self._days = days
    
    @property
    def id(self):
        return self.__id

    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value >= 5000:
            self.__price = value
        else:
            print('цена не может быть ниже 5000 сом')

    def book(self, client): # бронирует тур, делает его недоступным, если клиент оплатил.
        if self._is_booked:
            return False
        self._is_booked = True # делает его недоступным True-недоступно, False-доступно
        self._client = client
        return True

    def cancel_booking(self): #отменяет бронь, делает тур доступным.
        if not self._is_booked:
            return False
        self._is_booked = False #делает тур доступным
        self._client = None
        return True

    def info(self):
        return {
            'id': self.__id,
            'price': self.__price,
            'days': self._days,
            'is_booked': self._is_booked,
            'client': self._client, 
        }

class Client:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def pay(self, amount):
        if self.balance >= amount
            self.balance -= amount
            return True
        else:
            print(f"{self.name}, недостаточно средств для оплаты {amount} сом")
            return False
        
    def add_balance(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"{self.name} пополнил баланс на {amount} сом")
        else:
            print("Сумма должна быть положительной")

    def info(self):
        return f"Клиент: {self.name}, баланс: {self.balance} сом"



class Agency:
    def __init__(self, name):
        self.name = name
        self.tours = []
        self._income = 0

    def add_tour(self, tour):
        self.tours.append(tour)
        print(f"Тур {tour.id} добавлен в агентство {self.name}.")

    def add_tour(self, tour):
        self.tours.append(tour)
        print(f"Тур {tour.id} добавлен в агентство {self.name}.")

    def show_available_tours(self):
        available = [t for t in self.tours if not t._is_booked]
        if not available:
            print("Свободных туров нет")
        else:
            for t in available:
                print(f"Тур {tour.id}: {tour.price} сом, {tour._days} дней")

    def book_tour(self, client, tour_id):
        tour = next((t for t in self.tours if t.id == tour_id), None)
        if not tour:
            print(f"Тур с ID {tour_id} не найден")
            return False
        if tour._is_booked:
            print(f"Тур {tour_id} уже забронирован")
            return False
        if client.pay(tour.price):
            tour.book(client.name)
            self._income += tour.price
            print(f"Тур {tour_id} успешно забронирован клиентом {client.name}")
            return True
        else:
            print(f"Клиент {client.name} не смог оплатить тур {tour_id}")
            return False
        
    def cancel_all_bookings(self):
        for t in self.tours:
            if t._is_booked:
                t.cancel_booking()
        print("Все бронирования отменены")

    def show_status(self):
        print(f"Статус агентства {self.name}:")
        for t in self.tours:
            status = "Занят" if t._is_booked else "Свободен"
            client = t._client if t._client else "-"
            print(f"Тур {t.id}: {status}, клиент: {client}, цена: {t.price} сом")
        print(f"Текущая выручка: {self._income} сом")