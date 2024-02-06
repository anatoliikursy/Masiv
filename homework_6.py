class Car:
    def __init__(self, brand, model, __year, color):
        self.brand = brand
        self.model = model
        self.__year = self.__validate_year(__year)
        self.color = color

    def __validate_year(self, year): #валідність данних
        current_year = 2024
        if 1900 <= year <= current_year:
            return year
        else:
            print("Некоректний рік!")
            return self.__year
        
    def start(self):
        print("Автомобіль запустився.")

    def stop(self):
        print("Автомобіль зупинився.")

    def get_year(self):
        return self.__year

    def set_year(self, new_year):
        self.__year = self.__validate_year(new_year)

class ElectricCar(Car):
    def __init__(self, brand, model, __year, color, battery_size):
        super().__init__(brand, model, __year, color)
        self.battery_size = battery_size

    def start(self):
        print("Eлектромобіль запустився.")
        
    def stop(self):
        print("Eлектромобіль зупинився.")

# дати значення атрибутам
car1 = Car("Renault", "Clio", 2007, "Blue")
electric_car1 = ElectricCar("Renault", "Zoe", 2017, "Black", 41)

car1.start()
car1.stop()
electric_car1.start()
electric_car1.stop()

print(car1.get_year())
car1.set_year(2025)
print(car1.get_year())
car1.set_year(2010)
print(car1.get_year())