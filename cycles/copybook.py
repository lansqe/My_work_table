# a = 1
# b = 10
#
# result = 0
#
# for i in range(a, b+1):
#     if i % a == 3 or i % 5 == 0:
#         result += i
#
# print(result)

# num = 13
# count = 0
#
# if num > 1:
#     for i in range(1, num+1):
#         if num % i == 0:
#             count += 1
#
#
# print('это простое число' if count == 2 else 'это не простое число')

# numbers = [16, 32, 1, 7, -5, 256, 0, 1.3333, 15.5]
#
# for number in numbers:
#     if number < 1:
#         is_two_power = False
#     elif number == 1:
#         is_two_power = True
#     else:
#         while number % 2 == 0:
#             number //= 2
#         is_two_power = number == 1
#     print(is_two_power)




#    эспрессо = 7г молотого кофе
#    американо = 1 эспрессо
#    латте = 180мл молока и 1 эспрессо
#    капучино 100 мл молока и 1 эспрессо
# 1 посетитель = один напиток

#
# coffee_on_gram = 70
# milk_on_gram = 100
#
# num_drink = 0
# visitors = 0
#
#
# def milk_remaining(milk: float, name: str) -> float:
#     if name == 'латте':
#         milk -= 180
#         print('Был заказан латте')
#     elif name == 'капучино':
#         milk -= 100
#         print('Был заказан капучино')
#     else:
#         print('Был заказан американо')
#     return milk
#
#
# while milk_on_gram > 0 and coffee_on_gram > 0:
#     if num_drink == 3 or num_drink % 15 == 0:
#         name_drink = 'капучино'
#     elif num_drink == 5:
#         name_drink = 'латте'
#     else:
#         name_drink = 'американо'
#     num_drink += 1
#     coffee_on_gram -= 7
#     milk_remaining(milk_on_gram, name_drink)
#
# print(f'Осталось {milk_on_gram} мл. молока и {coffee_on_gram} гр. кофе')
# print(f'Посетителей пришло за смену: {num_drink}')



# grades = {"Математика": 4, "История": 3, "Биология": 3, "География": 4}


# def subject_high_grade(min_grade: int):
#     subjects = []
#     for lesson, grade in grades.items():
#         if grade >= 4:
#             subjects.append(lesson)
#     return subjects
#
# high_grade_subjects = subject_high_grade(4)
#
# print(f"Предметы с оценкой {4} и выше: {', '.join(high_grade_subjects)}")

# lst_1 = ["1", "0", "0", "1"]
# lst_2 = ["0", "1", "1", "0"]
# for a, b in zip(lst_1, lst_2):
#     print(a,b)

m = [[1, 2, 4],
     [3, 2, 1],
     [1, 3, 4]]

main = []
secondary = []

for i in range(len(m)):
    main.append(m[i][i])
    secondary.append(m[i-1][-i])

result = True if sum(main) == sum(secondary) else False
