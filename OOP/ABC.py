import re
from abc import ABC
from abc import abstractmethod
import math
from email_validator import validate_email, EmailNotValidError


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
    email = "my+address@example.org"

    def __init__(self, message: str, recipient: str):
        self.message = message
        self.recipient = recipient

    @abstractmethod
    def send(self, message: str, recipient: str):
        pass

    @abstractmethod
    def validate_recipient(self, recipient: str) -> bool:
        pass

    def notifire(self):
        if self.validate_recipient(self.message):
            self.send(self.message, self.recipient)
        else:
            print(f'Invalid recipient: {self.recipient}')


class EmailNotifier(Notifire):
    def validate_recipient(self, recipient: str) -> bool:
        email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(email_regex, recipient) is not None

    def send(self, message: str, recipient: str):
        return f'Sending email to {recipient}: {message}'


class SMSNotifier(Notifire):
    def validate_recipient(self, recipient: str) -> bool:
        phone_regex = r'^\+?[1-9]\d{1,14}$'
        return re.match(phone_regex, recipient) is not None

    def send(self, message: str, recipient: str):
        print(f"Sending SMS to {recipient}: {message}")


class PushNotifier(Notifire):
    def validate_recipient(self, recipient: str) -> bool:
        return bool(recipient.strip())

    def send(self, message: str, recipient: str):
        print(f"Sending push notification to {recipient}: {message}")
