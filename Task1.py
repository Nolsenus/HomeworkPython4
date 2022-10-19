def is_prime(num):
    for i in range(2, num // 2):
        if num % i == 0:
            return i
    return True


def get_prime_dividers(num):
    result = []
    if num < 0:
        num = -num
    if num <= 1:
        return result
    divider = is_prime(num)
    while divider is not True:
        result.append(divider)
        num //= divider
        divider = is_prime(num)
    result.append(num)
    return result


def main():
    try:
        num = int(input('Введите целое число: '))
        print(f'{num} -> {get_prime_dividers(num)}')
    except ValueError:
        print('Вы ввели не целое число.')


if __name__ == '__main__':
    main()
