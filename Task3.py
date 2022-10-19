import random


def make_polynomial(power):
    supers = ('\u2070', '\u00b9', '\u00b2', '\u00b3', '\u2074', '\u2075', '\u2076', '\u2077', '\u2078', '\u2079')
    # Первый коэффициэнт должен быть не нулевым, чтобы многочлен был степени power
    coefficient = random.randint(1, 100)
    result = str(coefficient) + '*x'
    for i in str(power):
        result += supers[int(i)]
    for i in range(power - 1, 1, -1):
        coefficient = random.randint(0, 100)
        if not coefficient == 0:
            result += ' + ' + str(coefficient) + '*x'
            for j in str(i):
                result += supers[int(j)]
    coefficient = random.randint(0, 100)
    if not coefficient == 0:
        result += ' + ' + str(coefficient) + '*x'
    result += ' = 0'
    return result


def main():
    try:
        power = int(input('Введите натуральное число - степень многочлена: '))
        file_name = 'task3_output.txt'
        result = f'{power} -> {make_polynomial(power)}'
        print(result)
        with open(file_name, 'w', encoding='utf-8') as file:
            file.write(result)
    except ValueError:
        print('Вы ввели не натуральное число.')


if __name__ == '__main__':
    main()
