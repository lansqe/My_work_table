from datetime import datetime
from datetime import date
from datetime import time
from datetime import timedelta


# print(d1.today())
# print(d1)
# print(d1.year)
# print(d1.month)
# print(d1.day)

d1 = date(2025, 2, 15)
d2 = date(2022, 3, 23)


def delta(data_1, data_2):
    delta_datatime = data_1 - data_2
    print(type(delta_datatime))
    return f'Разница составляет: {delta_datatime.days} дней'


print(delta(d1, d2))
