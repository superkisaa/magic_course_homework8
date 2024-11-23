# Создайте классы для представления структуры магазина техники.

# Требования:

# Базовый класс Device, который будет представлять общие атрибуты
# для любой техники:

# атрибуты: brand, model, price.
# метод get_info(), который возвращает строку с кратким описанием устройства.
# Дочерние классы:

# Laptop с дополнительными атрибутами ram и storage.
# Smartphone с атрибутами camera_megapixels и battery_capacity.

# Каждый из классов должен переопределить метод get_info()
# для включения специфичной информации.
# Создайте класс Store, содержащий список устройств:

# Метод add_device(device), который добавляет устройство в магазин.
# Метод list_devices(), который выводит информацию обо всех устройствах.

class Device:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

    def get_info(self):
        return f"Бренд: {self.brand}, модель: {self.model}, цена: {self.price}"


class Laptop(Device):
    def __init__(self, brand, model, price, ram, storage):
        super().__init__(brand, model, price)
        self.ram = ram
        self.storage = storage

    def get_info(self):
        origin = super().get_info()
        return origin + f", память: {self.ram}, хранилище: {self.storage}"


class Smartphone(Device):
    def __init__(self, brand, model, price, camera_megapixels, battery_capacity):
        super().__init__(brand, model, price)
        self.camera_megapixels = camera_megapixels
        self.battery_capacity = battery_capacity

    def get_info(self):
        origin = super().get_info()
        return origin + f", камера: {self.camera_megapixels}, батарея: {self.battery_capacity}"


class Store:
    def __init__(self):
        self.devices = []

    def add_device(self, device):
        self.devices.append(device)

    def list_devices(self):
        for device in self.devices:
            print(device.get_info())

lap = Laptop('Apple', "Mac2", "120000", 78, 100)
smart = Smartphone('Apple', 'Iphone', '50000', 100, 100)
store1 = Store()
store1.add_device(lap)
store1.list_devices()
store1.add_device(smart)
store1.list_devices()
