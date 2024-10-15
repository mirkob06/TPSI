class Car:
    total_cars = 0

    def __init__(self, model, brand, year, price):
        self.model = model
        self.brand = brand
        self.year = year
        self.price = price
        Car.total_cars += 1

    def display_details(self):
        print(f"Model: {self.model}, Brand: {self.brand}, Year: {self.year}, Price: ${self.price:.2f}")

    def calculate_depreciation(self, current_year=2024):  # Default current year set to 2024
        age = current_year - self.year
        depreciation_rate = 0.05
        depreciated_value = self.price * ((1 - depreciation_rate) ** age)
        return f"Depreciated value in {current_year}: ${depreciated_value:.2f}"

    @staticmethod
    def count_cars():
        return f"Total number of cars: {Car.total_cars}"

    @classmethod
    def compare_prices(cls, car1, car2):
        if car1.price > car2.price:
            return f"{car1.model} is more expensive than {car2.model}."
        elif car1.price < car2.price:
            return f"{car2.model} is more expensive than {car1.model}."
        else:
            return f"{car1.model} and {car2.model} have the same price."

    def compare_with(self, other_car):
        if self.price > other_car.price:
            result = f"{self.model} is more expensive than {other_car.model}."
        elif self.price < other_car.price:
            result = f"{other_car.model} is more expensive than {self.model}."
        else:
            result = f"{self.model} and {other_car.model} have the same price."

        if self.year > other_car.year:
            result += f" Also, {self.model} is newer than {other_car.model}."
        elif self.year < other_car.year:
            result += f" Also, {other_car.model} is newer than {self.model}."
        else:
            result += f" Both cars were produced in the same year."
        return result


car1 = Car("Model S", "Tesla", 2020, 79999)
car2 = Car("Mustang", "Ford", 2018, 55999)

car1.display_details()
car2.display_details()

print(car1.calculate_depreciation())
print(car2.calculate_depreciation())

print(Car.count_cars())

print(Car.compare_prices(car1, car2))

print(car1.compare_with(car2))
