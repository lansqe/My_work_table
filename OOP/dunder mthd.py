
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# При отсутствии метода __str__, при выводит: тип объекта и в какой ячейке памяти этот объект начинается
    # <__main__.Point object at 0x10289eed0>,
    def __str__(self):
        return f'Point x={self.x}, y={self.y}'
#              иначе выводит этот return


p = Point(10, 20)
# print(p)


class Road:

    def __init__(self, length):
        self.length = length

    # Выводит длину
    # Юзлес метод
    def __len__(self):
        return self.length

    def __str__(self):
        return f'A road of length: {self.length}'


    def __del__(self):
        print(f'The road has been destroyed')
    # Сбрасывает кол-во ссылок на обьект,
    # Исключения, возникающие в `__del__`, игнорируются
    # Оператор `del` не удаляет принудительно объект, а лишь освобождает переменную, уменьшая счетчик ссылок


# r = Road(100)
#
# print(len(r))
# print(r)
# del r


class Character:

    def __init__(self, race, damage = 100):
        self.race = race
        self.damage = damage

    def __repr__(self):
        return f'Character("{self.race}", {self.damage})'

    def __eq__(self, other):
        if isinstance(other, Character):
            return self.race == other.race and self.damage == other.damage
        return False

    def __ne__(self, other):
        pass


d = Character('Wolf')
c = eval(repr(d))
print(d)
print(c == d) # Метод __eq__ сравнивает содержимое объектов, при его отсутствии
              # он сравнивает две ссылки на объект


