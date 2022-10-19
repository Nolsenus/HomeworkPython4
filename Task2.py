def remove_duplicates(nums):
    unique = set({})
    for i in nums:
        if i not in unique:
            unique.add(i)
    return list(unique)


def main():
    string = input('Введите последовательность чисел через пробел: ')
    elements = string.split(' ')
    nums = []
    for i in elements:
        try:
            nums.append(float(i))
        except ValueError:
            print(f'{i} - не число.')
    print(f'Введённая строка - {string}')
    print(f'Неповторяющиеся числа из этой строки - {remove_duplicates(nums)}')


if __name__ == '__main__':
    main()
