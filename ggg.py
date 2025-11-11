class Person:
    def __init__(self, name, age, balance):
        self.name = name
        self.age = age
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Сумма пополнения должна быть положительной.")
            return
        self.balance += amount
        print(f"{self.name} пополнил счет на {amount:.2f} сом. Новый баланс {self.balance:.2f} сом")
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Сумма снятия должна быть положительной.")
            return
        if amount > self.balance:
            print("Недостаточно средств на счёте.")
            return
        self.balance -= amount
        print(f"{self.name} снял {amount:.2f} сом. Остаток на счете: {self.balance:.2f} сом.")

    def info(self) -> str:
        return f"Клиент: {self.name}, возраст: {self.age}, Баланс: {self.balance:.2f} сом"

class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = [] # список объектов Person
        self.products = [] # депозиты, кредиты, рассрочки
        self.income = 0 # доход бизнеса

    def add_client(self, client):
        if client not in self.clients:
            self.clients.append(client)
            print(f"Клиент {client.name} добавлен в банк {self.name}.")
        else:
            print(f"Клиент {client.name} уже зарегистрирован в банке {self.name}.")
    def add_product(self, product):
        self.products.append(product)
        print(f"Добавлен продукт: {product}.")
        if hassatr(product, "profit"):
            self.income += product.profit
    def add_income(self, income):
        if income > 0:
            self.income += income
            print(f"Доход банка увеличен на {income:.2f} сом. Текущий доход: {self.income:.2f} сом.")
        else:
            print("Доход должен быть положительным числом.")
    def calculate_total_profit(self):
        total = sum(getattr(p, "profit", 0) for p in self.products)
        self.income = total
        print(f"Общая прибыль банка {self.name}: {self.income:.2f} сом")
        return total
    def show_clients(self):
        if not self.clients:
            print("У банка пока нет клиентов.")
        else:
            print(f"Клиенты банка {self.name}: ")
            for c in self.clients:
                print(f" - {c.name}, баланс: {c.balance:.2f} сом")
    def show_products(self):
        if not self.products:
            print("Активных продуктов пока нет.")
        else:
            print(f"Продукты банка {self.name}: ")
            for p in self.products:
                print(f" - {p}")

class BankProduct:
    def __init__(self, client, amount, interes_rate, term_months):
        self.client = client
        self.amount = amount
        self.interes_rate = interes_rate
        self.term_months = term_months
        self.profiti = 0

    def calculate_interest(self):
        interest = self.amount * (self.interes_rate / 100) * (self.term_months / 12)
        return round(interest, 2)
    def info(self):
        return (f"Клиент: {self.client.name}, сумма: {self.amount:.2f} сом.," 
                f"Ставка: {self.interest_rate:.2f}%, срок: {self.term_months} мес.")
    def __str__(self):
        return f"{self.__class__.__name__}: {self.info()}"
    
class Deposit(BankProduct):
    def __init__(self, client, amount, interes_rate, term_months):
        super().__init__(client, amount, interes_rate, term_months)
        self.is_closed = False
        if client.balance >= amount:
            client.withdraw(amount)
            print(f"{client.name} открыл депозит на сумму {amount:.2f} сом.")
        else:
            raise ValueError(f"Недостаточно средств для открытия депозита у клиента {client.name}")
        self.profiti = 0
    def close_deposit(self):
        if self.is_closed:
            print("Депозит уже закрыт.")
            return
        
        interest = self.calculate_interest()
        total = self.amount + interest
        self.client.deposit(total) 

        self.profiti -= interest
        self.is_closed = True
        print(f"Депозит клиента {self.client.name} закрыт. Выплачено {total:.2f} сом. (включая {interest:.2f} сом. процентов).")
    def info(self):
        status = "закрыт" if self.is_closed else "активен"
        return (f"Депозит ({status}) - клиент: {self.client.name}, сумма: {self.amount:.2f} сом., "
                f"ставка: {self.interes_rate:.2f}%, срок: {self.term_months} мес.")
class Credit(BankProduct):
    def __init__(self, client, amount, interest_rate, term_months):
        super().__init__(client, amount, interest_rate, term_months)
        self.is_closed = False
        self.client.deposit(amount)
        print(f"{client.name} получил кредит на сумму {amount:.2f} сом. под {interest_rate:.2f}% на {term_months} мес.")
    def monthly_payment(self):
        if self.interest_rate == 0:
            return round(self.amount / self.term_months, 2)
        r = self.interest_rate / 100 / 12  
        n = self.term_months
        payment = self.amount * r / (1 - (1 + r) ** -n)
        return round(payment, 2)
    def close_credit(self):
        if self.is_closed:
            print("Кредит уже закрыт.")
            return
        total_payment = self.monthly_payment() * self.term_months
        overpayment = round(total_payment - self.amount, 2)
        if self.client.balance >= total_payment:
            self.client.withdraw(total_payment)
            print(f"{self.client.name} полностью погасил кредит.")
        else:
            raise ValueError(f"Недостаточно средств для закрытия кредита у клиента {self.client.name}.")
        self.profit = overpayment
        self.is_closed = True
        print(f"Кредит закрыт. Банк получил прибыль {self.profit:.2f} сом. (проценты).")
    def info(self):
        status = "закрыт" if self.is_closed else "активен"
        return (f"Кредит ({status}) — клиент: {self.client.name}, сумма: {self.amount:.2f} сом., "
                f"ставка: {self.interest_rate:.2f}%, срок: {self.term_months} мес., "
                f"ежемес. платёж: {self.monthly_payment():.2f} сом.")
class Installment(BankProduct):
    def __init__(self, client, amount, term_months, product_name, commission_rate):
        super().__init__(client, amount, interest_rate=0, term_months=term_months)
        self.product_name = product_name
        self.commission_rate = commission_rate  # комиссия банка (% от суммы товара)
        self.is_closed = False
        print(f"{client.name} оформил рассрочку на товар '{product_name}' стоимостью {amount:.2f} сом. "
              f"на {term_months} мес. (комиссия банка {commission_rate:.2f}%).")
        self.profit = round(self.amount * (self.commission_rate / 100), 2)
    def monthly_payment(self):
        payment = round(self.amount / self.term_months, 2)
        return payment
    def close_installment(self):
        if self.is_closed:
            print("Рассрочка уже закрыта.")
            return
        total_payment = self.amount
        if self.client.balance >= total_payment:
            self.client.withdraw(total_payment)
            print(f"{self.client.name} полностью оплатил товар '{self.product_name}'.")
        else:
            raise ValueError(f"Недостаточно средств для закрытия рассрочки у клиента {self.client.name}.")
        print(f"Банк получил комиссию {self.profit:.2f} руб. по рассрочке '{self.product_name}'.")
        self.is_closed = True
    def info(self):
        status = "закрыта" if self.is_closed else "активна"
        return (f"Рассрочка ({status}) — клиент: {self.client.name}, товар: '{self.product_name}', "
                f"сумма: {self.amount:.2f} сом., срок: {self.term_months} мес., "
                f"комиссия: {self.commission_rate:.2f}%, ежемес. платёж: {self.monthly_payment():.2f} сом.")