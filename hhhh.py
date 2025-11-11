class Computer:
    def __init__(self, comp_id, hourly_rate):
        self.__id = comp_id
        self.__hourly_rate = hourly_rate
        self._is_busy = False
        self._currer_client = None
        self._hours = 0

    @property
    def id(self):
        return self.__id
    @property
    def hourly_rate(self):
        return self.__hourly_rate
    @hourly_rate.setter
    def hourly_rate(self, new_rate):
        if new_rate >=50 and new_rate <=1000:
            self.__hourly_rate = new_rate
            return self.__hourly_rate
        
    def start_session(self, client, hours):
        if self._is_busy:
            print(f"Компьютер {self.id} занят.")
            return False
        cost = self.__hourly_rate * hours
        if client.pay(cost):
            self._is_busy = True
            self._currer_client = client
            self._hours = hours
            print(f"{client.name} начал сессию.")
            return True
        else:
            print(f"Не хватает денег {client}")
    def end_session(self):
        self._is_busy = False
        income = self.__hourly_rate * self._hours
        client_name = self._currer_client.name
        print(f"Сессия завершена {client_name}")
        self._currer_client = None
        self._hours = 0
        return income
    def info(self):
        status = "занят" if self._is_busy else "свободен"
        print(f"Комп {self.id}:{status}")

class Client:
    def __init__(self, name, balance):
        self.name = name
        self._balance = balance

    @property
    def balance(self):
        return self._balance
    
    def add_balance(self, amount):
        if amount >0 and amount<=10000:
            self._balance += amount
            print(f"Баланс пополнен на {amount}сом, теперь у вас {self._balance} сом")
        else:
            print("Введите корректное значение на пополнение.")
            return False
        
    def pay(self, amount):
        if amount <= 0:
            print("Сумма должна быть положительной.")
            return False
        if amount > self._balance:
            print(f"Недостаточно средств. На карте {self._balance} сом")
            return False
        self._balance -+ amount
        print(f"Оплачено {amount} сом. Остаток: {self._balance} сом")
        return True
    def info(self):
        print(f"Имя: {self.name} на карте: {self._balance} сом")
class Club:
    def __init__(self, name):
        self.name = name
        self.computers = []
        self._income = 0

    def add_computer(self, computer):
        self.computers.append(computer)
    def find_free_computer(self):
        for comp in self.computers:
            if not comp._is_busy:
                return comp
            return None
    def serve_client(self, client, hours):
        comp = self.find_free_computer()
        if not comp:
            print("Нет свободных компьютеров")
            return False
        if comp.start_session(client, hours):
            print(f"{client.name} обслуживается на компе {comp.id}")
            return True
        return False
    
    def end_all_session(self):
        for comp in self.computers:
            if comp._is_busy:
                self._income += comp.end_session()

    def show_status(self):
        print(f"\nКлуб '{self.name}': доход {self._income} сом")
        for comp in self.computers:
            comp.info()