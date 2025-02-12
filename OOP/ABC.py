from abc import ABC
from abc import abstractmethod
import math


class Shape(ABC):

    def __init__(self):
        super().__init__()

    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        print('calc perimeter')
        # pass

    def drag(self):
        print('Basic dragging functionality')


#s = Shape() #Невозможно создать экземпляр абстрактного класса Shape без реализации его методов area, draw, perimeter


class Triangle(Shape):

    def __init__(self, a: int, b: int, c: int):
        super().__init__()
        self.a = a
        self.b = b
        self.c = c

    def draw(self):
        print(f'drawing triangle with sides={self.a}, {self.b}, {self.c}')

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def perimeter(self):
        super().perimeter()
        return self.a + self.b + self.c

    def drag(self):
        super().drag()
        print('Additional actions')


# t = Triangle(3, 4, 5)
# print(t.perimeter())
# t.drag()


# HW _1_


class Notifire:

    def __init__(self, message: str, recipient: str):
        self.message = message
        self.recipient = recipient

    def send(self, message: str, recipient: str):
        pass

    def validate_recipient(self, recipient: str) -> bool:
        pass

    def notifire(self, message: str, recipient: str):
        if self.validate_recipient(message):
            self.send(message, recipient)
        else:
            print('Invalid recipient')

# Подклассы `EmailNotifier`, `SMSNotifier`, `PushNotifier`:
# 	•	Создайте классы `EmailNotifier`, `SMSNotifier` и `PushNotifier`, которые наследуются от `Notifier`.
# 	•	Реализуйте абстрактные методы `send` и `validate_recipient` в каждом подклассе, учитывая особенности отправки уведомлений каждым способом.
# 	•	`EmailNotifier`:
# 	•	`validate_recipient`: Проверяет, является ли `recipient` валидным email-адресом (используйте регулярные выражения или сторонние библиотеки для валидации).
# 	•	`send`: Имитирует отправку email (просто печатает сообщение “Sending email to {recipient}: {message}”).
# 	•	`SMSNotifier`:
# 	•	`validate_recipient`: Проверяет, является ли `recipient` валидным номером телефона (используйте регулярные выражения или сторонние библиотеки для валидации).
# 	•	`send`: Имитирует отправку SMS (просто печатает сообщение “Sending SMS to {recipient}: {message}”).
# 	•	`PushNotifier`:
# 	•	`validate_recipient`: Проверяет, является ли `recipient` валидным токеном устройства для push-уведомлений (просто проверяет, что строка не пустая).
# 	•	`send`: Имитирует отправку push-уведомления (просто печатает сообщение “Sending push notification to {recipient}: {message}”).

# •	Создайте экземпляры каждого из `Notifier`’ов.
# 	•	Попробуйте отправить уведомления с валидными и невалидными получателями, чтобы проверить работу системы.