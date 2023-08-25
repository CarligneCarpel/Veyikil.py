import datetime

class Vehicle:
    def __init__(self, make, model, year, daily_rate):
        self.make = make
        self.model = model
        self.year = year
        self.daily_rate = daily_rate

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Daily Rate: ${self.daily_rate:.2f}")

class Car(Vehicle):
    def __init__(self, make, model, year, daily_rate, num_seats):
        super().__init__(make, model, year, daily_rate)
        self.num_seats = num_seats

    def display_info(self):
        super().display_info()
        print(f"Number of Seats: {self.num_seats}")

class Motorcycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, engine_type):
        super().__init__(make, model, year, daily_rate)
        self.engine_type = engine_type

    def display_info(self):
        super().display_info()
        print(f"Engine Type: {self.engine_type}")

class Bicycle(Vehicle):
    def __init__(self, make, model, year, daily_rate, frame_type):
        super().__init__(make, model, year, daily_rate)
        self.frame_type = frame_type

    def display_info(self):
        super().display_info()
        print(f"Frame Type: {self.frame_type}")

class Rental:
    def __init__(self, vehicle, start_date, end_date):
        self.vehicle = vehicle
        self.start_date = start_date
        self.end_date = end_date

    def calculate_total_price(self):
        num_days = (self.end_date - self.start_date).days
        total_price = num_days * self.vehicle.daily_rate
        return total_price

    def display_rental_info(self):
        print("Rental Information:")
        print("------------------------------")
        print("Rental Period:", self.start_date, "to", self.end_date)
        self.vehicle.display_info()
        print("Total Price:", self.calculate_total_price())

# Kòd ki soti pi wo (ekri kòd la nan anviwònman ou)

# Kreye yon objè Rental ak yon machin
car = Car("Toyota", "Camry", 2023, 50.0, 5)
rental_start = datetime.date(2023, 8, 25)
rental_end = datetime.date(2023, 8, 30)
rental = Rental(car, rental_start, rental_end)

# Afiche detay sou lwe a ak pri total la
rental.display_rental_info()
