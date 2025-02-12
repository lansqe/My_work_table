
class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

# При отсутствии метода __str__, при выводит следующее: <__main__.Point object at 0x10289eed0>,
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

    # Сбрасывает кол-во ссылок на обьект,
    # Исключения, возникающие в `__del__`, игнорируются
    # Оператор `del` не удаляет принудительно объект, а лишь освобождает переменную, уменьшая счетчик ссылок
    def __del__(self):
        print(f'The road has been destroyed')


r = Road(100)

print(len(r))
print(r)
del r

