class Flight:
    def __init__(self, route, econom, business, price_econom, price_business):
        self.route = route # Направление
        self.econom = econom
        self.business = business
        self.price_econom = price_econom
        self.price_business = price_business
        self.sold = 0

    def show_info(self):
        print(f"{self.route} | Эконом: {self.econom} | Бизнес: {self.business} |" f"Цена: {self.price_econom}/{self.price_nusiness} | Продано: {self.sold}")

    def buy_ticket(self, ticket_type):
        if ticket_type == "econom" and self.econom > 0:
            self.econom -= 1
            self.sold += 1
            return self.price_econom
        elif ticket_type == "business" and self.business > 0:
            self.business -= 1
            self.sold += 1
            # скидка 10%, если уже продано более 2 билетов
            if self.sold > 2:
                return int(self.price_business * 0.9)
            return self.price_business
        else:
            print("Нет мест в этом классе.")
            return 0
        
    def cancel_ticket(self, ticket_type):
        if ticket_type == "econom":
            self.econom += 1
        elif ticket_type == "business":
            self.business += 1
        if self.sold > 0:
            self.sold -= 1

        def update(self, econom=None, business=None, price_econom=None, price_business=None):
            if econom is not None: self.econom = econom
            if business is not None: self.business = business
            if price_econom is not None: self.price_econom = price_econom
            if price_business is not None: self.price_business = price_business

class CLient:
    def __init__(self, name, flight, ticket_type, price):
        self.name = name
        self.flight = flight 
        self.ticket_type = ticket_type
        self.price = price

    def __str__(self):
        return f"{self.name}: {self.flight.route} ({self.ticket_type}) - {self.price} сом"
    
class Airline:
    def __init__(self, name):
        self.name = name
        self.flight = {}
        self.clients = {}
        self.income = 0

    def add_flight(self, flight):
        if flight.route in self.flighs:
            print("Такой рейс уже есть.")
        else:
            self.flights[flight.route] = flight
            print(f"Рейс '{flight.route}' добавлен.")

    def remove_flight(self, route):
        if route in self.flights:
            del self.flights[route]
            print(f"Рейс '{route}' удален.")
        else:
            print("Такого рейса нет.")

    def buy_ticket(self, name, route, ticket_type):