from dataclasses import dataclass
# Создайте классы Employee HourlyEmployee и SalariedEmployee
import dataclasses
from abc import ABC, abstractmethod


class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass


@dataclass
class HourlyEmployee(Employee):
    hours_worked: int
    hourly_rate: int

    def calculate_salary(self):
        return self.hours_worked * self.hourly_rate


@dataclass
class SalariedEmployee(Employee):
    monthly_salary: int

    def calculate_salary(self):
        return self.monthly_salary


# Код для проверки

hourly_employee = HourlyEmployee(100, 25)
assert hourly_employee.hours_worked == 100
assert hourly_employee.hourly_rate == 25
assert hourly_employee.calculate_salary() == 2500

salaried_employee = SalariedEmployee(4000)
assert salaried_employee.monthly_salary == 4000
assert salaried_employee.calculate_salary() == 4000
print('Good')