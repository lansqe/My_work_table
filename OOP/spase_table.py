class Name:

    def __init__(self, rough_first_name: str, rough_last_name: str):
        self.rough_first_name = rough_first_name
        self.rough_last_name = rough_last_name

    def first_name(self):
        return self.rough_first_name.capitalize()

    def last_name(self):
        return self.rough_last_name.capitalize()

    def full_name(self):
        full_first_name = self.rough_first_name.capitalize()
        full_last_name = self.rough_last_name.capitalize()
        return f'{full_first_name} {full_last_name}'

    def initial(self):
        first_initial = self.rough_last_name[0].upper()
        last_initial = self.rough_last_name[0].upper()
        return f'{first_initial}.{last_initial}.'


unit = Name('viKtoR', 'veZUvi')


class Calculator:

    def __init__(self, first_number: float, second_numbers: float):
        self.first_number = first_number
        self.second_number = second_numbers

    def add(self):
        return self.first_number + self.second_number

    def subtract(self):
        return self.first_number - self.second_number

    def multiply(self):
        return self.first_number * self.second_number

    def divide(self):
        if self.second_number == 0:
            raise ValueError('Деление на ноль невозможно')
        return self.first_number / self.second_number


# var_one = Calculator(10, 0)
# print(var_one.add())
# print(var_one.subtract())
# print(var_one.multiply())
# try:
#     print(var_one.divide())
# except ValueError as e:
#     print(e)


class Employee:
    def __init__(self, first_name: str, last_name: str, salary: float):
        self.first_name = first_name.title()
        self.last_name = last_name.title()
        self.salary = salary

    @classmethod
    def from_string(cls, parse):
        data = parse.split('-')
        return cls(data[0], data[1], data[2])


emp1 = Employee('maRy', 'silveR', 88000.0)
emp2 = Employee.from_string('ruSl-EmbO-71000.0')

print(emp1.first_name)
print(emp1.salary)
print(emp2.first_name)
print(emp2.salary)