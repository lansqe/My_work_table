class Name():

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



class Calculator():

    def __init__(self, first_number, second_numbers):
        self.first_number = first_number
        self.second_number = second_numbers

    def add(self):
        pass

    def subtract(self):
        pass

    def multiply(self):
        pass

    def divide(self):
        pass