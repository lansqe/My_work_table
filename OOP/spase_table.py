import math


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


# emp1 = Employee('maRy', 'silveR', 88000.0)
# emp2 = Employee.from_string('ruSl-EmbO-71000.0')

# print(emp1.first_name)
# print(emp1.salary)
# print(emp2.first_name)
# print(emp2.salary)


class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    @classmethod
    def parse_book_info(cls, book_info):
        title, author, year = book_info.split('-')
        return f'Title: {title}, Author: {author}, Year: {year}'


b1 = Book('Crime and Punishment', 'Fedor Dostoevsky', 1866)
b2 = Book.parse_book_info('Crime and Punishment-Fedor Dostoevsky-1866')


# print(b1.author)
# print(b2)


class Pizza:
    order_count = 0

    def __init__(self, ingredients: list):
        self.ingredients = ingredients
        Pizza.order_count += 1
        self.order_number = Pizza.order_count

    @classmethod
    def garden_feast(cls):
        return cls(['spinach', 'olives', 'mushroom'])

    @classmethod
    def meat_festival(cls):
        return cls(['beef', 'meatball', 'bacon'])

    @classmethod
    def hawaiian(cls):
        return cls(['ham', 'pineapple'])


# p1 = Pizza(['bacon', 'parmesan', 'ham'])
# p2 = Pizza.garden_feast()
#
# print(p1.ingredients)
# print(p2.ingredients)
#
# print(p1.order_number)
# print(p2.order_number)


class Circle:

    def __init__(self, radius):
        self.radius = radius

    def get_area(self):
        return f'Площадь круга: {self.radius**2 * math.pi}'

    def get_perimetr(self):
        return f'Длина окружности: {self.radius * math.pi * 2}'


# circle = Circle(10)
# area = circle.get_area()
# perimetr = circle.get_perimetr()
#
# print(area)
# print(perimetr)

class Beverage:
    prices = {'Strawberries': 1.5,
              'Banana': 0.5,
              'Mango': 2.5,
              'Blueberries': 1.0,
              'Apples': 1.75,
              'Pineapple': 3.5,
              'Raspberries': 1.0}

    def __init__(self, ingredients):
        if isinstance(ingredients, str):
            self.ingredients = [ingredients]
        else:
            self.ingredients = ingredients

    def get_cost(self):
        total_price = 0
        for ingredient in self.ingredients:
            if ingredient in self.prices:
                total_price += self.prices[ingredient]
        return f'Себестоимость напитка составляет: {total_price} '

    def get_price(self):
        total_price = 0
        for ingredient in self.ingredients:
            if ingredient in self.prices:
                total_price += self.prices[ingredient] * 2.5


        return f'Стоимость напитка составляет: {total_price}'

    def get_name(self):
        name_sort = []
        for ingredient in self.ingredients:
             if ingredient in self.prices:
                name = ingredient
                if name.endswith('berries'):
                    name = name[:-7] + 'berry'
                name_sort.append(name)

        name_sort = sorted(name_sort)

        name_sort.append('Fusion') if len(name_sort) > 1 else name_sort.append('Smoothe')

        return f'Ингредиенты входящие в состав напитка: {", ".join(name_sort)}'


s1 = Beverage('Banana')
print(s1.ingredients)
print(s1.get_cost())
print(s1.get_price())
print(s1.get_name())

s2 = Beverage(['Raspberries', 'Strawberries', 'Blueberries'])
print(s2.ingredients)
print(s2.get_cost())
print(s2.get_price())
print(s2.get_name())
