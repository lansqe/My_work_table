
import random

def create_number_file(filename="numbers.txt", num_lines=800, min_value=-999999, max_value=999999):
    """Создает текстовый файл с заданным количеством случайных целых чисел."""
    try:
        with open(filename, 'w') as f:
            for _ in range(num_lines):
                number = random.randint(min_value, max_value)
                f.write(str(number) + '\n')
        print(f"Файл '{filename}' успешно создан.")
    except Exception as e:
        print(f"Ошибка при создании файла: {e}")


def read_ints(path):
    lst = []
    try:
        with open(path, 'r') as f:
            for line in f:
                lst.append(int(line.strip()))
        return lst
    except FileNotFoundError:
        print(f"Ошибка: Файл '{path}' не найден.")
        return None
    except ValueError:
        print(f"Ошибка: Не удалось преобразовать строку в число в файле '{path}'.")
        return None
    except Exception as e:
        print(f"Ошибка при чтении файла: {e}")
    return None


def count_three_sum(ints):
    print('started count_three_sum')

    n = len(ints)
    counter = 0

    for i in range(n):
        for j in range(i+1, n):
            for k in range(j+1, n):
                if ints[i] + ints[j] + ints[k] == 0:
                    counter += 1
                    print(f'Triple found: {ints[i]}, {ints[j]}, {ints[k]}', end='\n')

    print(f'ended count_three_sum. Triple counter={counter}')

#
# if __name__ == '__main__':
#     print('started main')
#
#     create_number_file()
#     ints = read_ints('numbers.txt')
#     if ints:
#         count_three_sum(ints)
#
#     print('ended main')

#Продолжить - создать пару подклассов 13.02