# Создайте класс Employee, который инкапсулирует следующие данные:

# Приватные поля __name, __position, __salary.
# Методы set_name, set_position и set_salary для изменения значений
# этих полей (например, при повышении сотрудника).
# Ограничьте прямой доступ к __salary, добавив проверку,
# чтобы зарплату можно было изменить только через метод, например,
# при повышении. Запрещается устанавливать зарплату ниже текущего значения.

# Метод get_employee_info, который возвращает информацию о сотруднике в
# виде строки.

class Employee:
    def __init__(self, name, position, salary):
        self.__name = name
        self.__position = position
        self.__salary = salary


    def set_name(self, new_name):
        self.__name = new_name

    def set_position(self, new_position, new_salary = None):
        self.__position = new_position
        if new_salary is not None:
            self.__set_salary(new_salary)

    def __set_salary(self, new_salary):
        if new_salary > self.__salary:
            self.__salary = new_salary
        else:
            print("Запрещается устанавливать зарплату ниже текущего значения")

    def get_employee_info(self):
        return f"Имя: {self.__name}, Позиция: {self.__position}, Зарплата: {self.__salary}"


emp1 = Employee('Alena B', 'analyst', '70000')
#emp1.set_salary('60000')
emp1.set_position('middle analyst', '60000')
emp1.set_position('middle analyst', '80000')
emp1.set_name('Alena C')
print(emp1.get_employee_info())

