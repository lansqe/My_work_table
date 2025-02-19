from enum import Enum


class WeekDays(Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7


def show_day_name(day):
    weekday = WeekDays(day)
    return weekday.name, weekday


print(show_day_name(1))

