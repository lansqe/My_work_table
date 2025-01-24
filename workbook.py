# price_new = 54
# price_old = 94
#
# procent_izmeneniya = abs(((price_new - price_old) / price_old) * 100)
# result = round(procent_izmeneniya, 2)
# if result == 42.55:
#     print('Задача решена верно!')

# string1 = '\'Манчестер Юнайтед\' - чемпион Англии!\n2013'
# print(string1)

# square = "/* * * */ \n * * * * //n * * * * //n * * * *"
# print(square)

# my_list = [1, 2, 2, 3, 2]
# count = my_list.count(2)
# print(count) # 3
# my_list = [1, 2, 3, 4, 5]
#
# first_item = my_list.pop(0)
# last_item = my_list[-1]
# reversed_list = sorted(my_list, reverse=True)
# even_items = my_list[2::2]
#
# print(first_item, last_item, reversed_list, even_items, sep='\n')

# var_1 = list(range(-100,101,1))
# var_2 = list(range(250,-1,-2))
# var_3 = list(range(101,201,2))
# print(var_1, var_2, var_3, sep='\n' )
#
# a = 0
# b = 1
# result = list(range(a, b+1))
# total = sum(result)
# print(total)
# my_list = [1, 10, 0, 10, 11]
# eleven_index = my_list.index(11)
# ten_count = my_list.count(10)
#
# print(eleven_index, ten_count)

# student_names = ['Maria', 'Igor', 'Vladislav', 'Anna', 'Anatoly', 'Oksana']
#
# student_names.append('Anatoly')
# student_names.append('Oksana')
# scores = list(range(11))
# scores.pop(1)
# scores.pop(3)
# scores.pop(-1)
# lessons = ['Maria', 'Igor', 'Vladislav', 'Anna', 'Anatoly', 'Oksana']
# lessons.sort()
#
# print(student_names, scores, lessons, sep='\n')
# numbers_list = [1, 1, 2, 2, 3, 3, 4, 4]
# numbers_list_ordered = sorted(numbers_list, reverse=True)
# numbers_set = set(numbers_list)
# max_number = max(numbers_set)
# numbers_set.add(max_number + 1)
# min_number = min(numbers_list)
# numbers_list_copy = numbers_list.copy()
# numbers_list_copy.remove(min_number)
# numbers_frozenset = frozenset(numbers_list_copy)
#
# print(numbers_list_ordered, numbers_set, numbers_frozenset, sep='\n')
# list_1 = [1, 5, 3]
# list_2 = [2, 8]
# list_1.sort()
# list_2.sort(reverse=True)
# list_3 = list_1 + list_2
# list_3_len = len(list_3)
#
# print(list_1,list_2,list_3,list_3_len, sep='\nww')

# menu = {'White Chocolate Mocha', 'Americano', 'Flat White', 'Latte',
#         'Blueberry Muffin', 'Chocolate Chip Cookie'}
# stop = {'White Chocolate Mocha', 'Blueberry Muffin'}
#
# menu_today = menu
#
#
# print(menu_today)


# da_students = {'Ivanov Alexander', 'Loginov Vladislav', 'Ershova Anna', 'Korneva Daria'}
# dv_students = {'Ershova Anna', 'Egunov Andrey', 'Ignatov Alexey', 'Loginov Vladislav'}
#
# students = da_students
# # students.add(da_students)
#
# print(students)

#
# a = [1, 2, 4, 3]
#
# len_a = len(a) // 2
# a_1 = a[len_a-1]
#
# print(a_1)
# a = [1, 2, 2, 1, 3, 2, 3]
# b=1
# a.remove(b)
# a1 = a.copy()
# a1.reverse()
# a1.re(b)
# a=a1
#
# print(a)

# cities = ['Москва', 'Париж', 'Токио']
# peoples = [float(11.98), float(2.16), float(13.96)]
# cities_population = dict.fromkeys(cities, peoples)
#
#
# print(cities_population)

# data = {
#   "cost_price": 225.89,
#   "sell_price": 550.00,
#   "eclairs": 100
# }
# profit = data['sell_price'] - data['cost_price']
# profit_all = profit * data['eclairs']
# print(profit_all)

# student = {"name": "Igor", "notes": [4, 5, 4]}
# max_note = max(student['notes'])
# result = {
#   'name': student['name'], 'max_note': max_note
# }
# print(result)

# input_dict = {"морковь": 10.44, "капуста": 5.06, "клубника": 3}
#
# result = list(input_dict.values())
#
# print(sum(result))

# str_1 = 'Aa'
# str_2 = 'AaB'
# is_the_same_letters = str_2 == set(str_1)
# print(is_the_same_letters, str_2, set(str_1), sep='\n')

# x = '2.002'
# decimal_part = x.split('.')[0]
# print(decimal_part)

# str_1 = "кот"
# str_2 = "ток"
# result = str_1[::-1].capitalize() == str_2[::-1].capitalize()
# print(str_1[::-1].capitalize(), str_2[::-1].capitalize(), sep='\n')

# x = 'У лукоморья дуб зелёный'
#
# result = ' '.join(sorted(x.split()))
#

# x = 'На подоконнике в гостиной у бабушки росли цветы, цветы были красные и желтые, очень красивые цветы.'
# y = 'цветы'
# result = x.count(y)
# print(result)

# card = '5468350018455833'
#
# last_digit = card[-4:]
# len_card = len(card) - 4
# result = (len_card * '*') + last_digit

# a = 'Я помню чудное мгновенье'
# b = 'о'
# result = ''.join(a.split(b))
# print(result)


# entrance = input().split()
# # output =
# print(entrance)


# phone_number = '1234567890'
# parts = [
#     f'({phone_number[:3]})',
#         phone_number[3:6],
#         phone_number[6:]
#     ]
# print(''.join(parts))

# a = 3
# b = 5
# c = 4
#
# result = True if c**2 == (a**2 + b**2) else False
# print(result)


orders = [
    {"номер": "001", "клиент": "John", "дата": "2022-01-01", "статус": "в обработке"},
    {"номер": "002", "клиент": "Alice", "дата": "2022-01-02", "статус": "выполнен"},
    {"номер": "003", "клиент": "Bob", "дата": "2022-01-03", "статус": "выполнен"},
    {"номер": "004", "клиент": "Eva", "дата": "2022-01-04", "статус": "в обработке"},
]
for index, order in enumerate(orders, start=1):
    print(f"Заказ {index}:")
    for key, value in order.items():
        print(f"{key}: {value}")
    print()


