def sum_numbers(*args):
    return sum(args)


# d1 = sum_numbers(2,3)
# print(d1)


def describe_person(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')


# describe_person(name="Alice", age=30, city="New York")


def print_info(*args, **kwargs):
    print(args)
    print(kwargs)


# print_info(1, 2, 3, name="Bob", age=25)


def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result


#
# product = multiply(2, 3, 4)
# print(product)


def compare_dicts(**kwargs):
    dict1 = kwargs.get('dict1', {})
    dict2 = kwargs.get('dict2', {})

    for key in dict1.keys():
        if key in dict2:
            print(f'{key}: {dict1[key]} vs {dict2[key]}')
        else:
            print(f"{key}: {dict1[key]} (только в первом словаре)")

    for key in dict2.keys():
        if key not in dict1:
            print(f"{key}: {dict2[key]} (только во втором словаре)")


# compare_dicts(dict1={'a': 1, 'b': 2}, dict2={'b': 3, 'c': 4})


# '** or *'

def merge_list(*args):
    # x = [int(m) for m in args]
    for index, value in enumerate(args):
        num = args[index] + args[index - 1]
        return num


# lists = [1, 2, 3], [4, 5], [6]
# result = merge_list(*lists)
#
# print(result)

# def format_user_data(*args, **kwargs):
#     for dict_one, dict_two in args:
#     return kwargs


users = [
    {'name': 'Alice', 'age': 25, 'city': 'Moscow'},
    {'name': 'Bob', 'age': 30, 'city': 'London'},
]

# formatted = format_user_data(*users)
# print(*formatted)
# Вывод:
# Имя: Alice, Возраст: 25, Город: Moscow
# Имя: Bob, Возраст: 30, Город: London

import sys

arr_1 = []
arr_2 = arr_1
# print(sys.getrefcount(arr_1))

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = ['mad', 'her', 'ser', 'qwe', 'sqr', 'ale']
sqrt_num = list(map(lambda x: x ** 2, list_1))

# print(sqrt_num)

numbers = zip(list_1, list_2)


# print(dict(numbers))


def solve_hanoi_tower(num):
    if num <= 0:
        return 0
    else:
        return (2 ** num) - 1


solv = solve_hanoi_tower(5)


# print(solv)


def calc_dice_scores(lst):
    sum_num = 0
    for num in lst:
        if num[0] == num[1]:
            print('Ничья')
    return


# test = calc_dice_scores([(4,4), (2,4), (1,2)])
# print(test)


from functools import wraps


def log_decorator(func):
    @wraps(func)
    def wrap(*args, **kwargs):
        print(f'Calling func "{func}"')
        func(*args, **kwargs)
        print(f'Func "{func}" finished its work')

    return wrap


@log_decorator
def hello():
    print('Hello, world')


# hello()
# print()
# help(hello)
#

def any_duplicated(num: list[list[int]]) -> bool:

    seen = set()

    for sublist in num:
        for number in sublist:
            if number in seen:
                return True
            seen.add(number)
    return False


def duplicated(square):
    plain = [i for x in square for i in x]
    return sorted(plain) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


print(duplicated([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(duplicated([[1, 2, 3], [3, 5, 6], [7, 8, 9]]))


# Datatime?