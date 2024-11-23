# Создайте класс Vehicle, представляющий транспортное средство.
# Этот класс должен содержать:

# Поля make, model и year.
# Метод get_info, возвращающий строку с информацией о транспортном средстве.

# Затем создайте подклассы Car и Motorcycle, которые расширяют класс Vehicle:
# Класс Car должен иметь поле number_of_doors и метод get_info,
# который добавляет информацию о количестве дверей.
# Класс Motorcycle должен иметь поле has_sidecar (True или False)
# и метод get_info, который указывает, есть ли у мотоцикла коляска.

class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"Модель: {self.model}, год: {self.year}"

class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors

    def get_info(self):
        origin = (super().get_info())
        return origin + f" количество дверей: {self.number_of_doors}"


class Motorcycle(Vehicle):
    def __init__(self, make, model, year, has_sidecar: bool):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar

    def get_info(self):
        origin = (super().get_info())
        if self.has_sidecar:
            return origin + "коляска есть"
        return origin + ", коляски нет"

vehicle = Vehicle('Russia', 'transport', 2)
print(vehicle.get_info())

car = Car('Russia','Lada', 1, 2)
print(car.get_info())

moto = Motorcycle('USA', 'Harley', '883', False)
print(moto.get_info())


