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

numbers = [16, 32, 1, 7, -5, 256, 0, 1.3333, 15.5]

for number in numbers:
    if number < 1:
        is_two_power = False
    elif number == 1:
        is_two_power = True
    else:
        while number % 2 == 0:
            number //= 2
        is_two_power = number == 1
    print(is_two_power)




#    эспрессо = 7г молотого кофе
#    американо = 1 эспрессо
#    латте = 180мл молока и 1 эспрессо
#    капучино 100 мл молока и 1 эспрессо
# 1 посетитель = один напиток


coffee = 0.2 * 1000
milk = 3.0 * 1000

num_dink = 0
def milk_remaining(milk):


while milk > 0 and coffee > 0:
    if num_dink == 3 or num_dink % 3 == 0 and num_dink % 5 == 0:
        name_drink = 'капучино'
    elif num_dink == 5:
        name_drink = 'латте'
    else:
        name_dink = 'американо'
    num_dink += 1
    coffee -= 0.007
    if num
    milk -= 180 if name_drink == 'латте' else 100


print(coffee, milk)


visitors = 0
