import math
import re


def solve_quadratic(equation):
    equation = equation.replace('*', '')
    left_side = equation.split('=')[0]
    left_side = left_side.split('x^2')
    if left_side[0] == '':
        a = 1
    elif left_side[0] == '-':
        a = -1
    else:
        a = float(left_side[0])
    if not left_side[1] == '':
        if 'x' in left_side[1]:
            left_side = left_side[1].split('x')
            if left_side[0] == '+':
                b = 1
            elif left_side == '-':
                b = -1
            else:
                b = float(left_side[0])
            if not left_side[1] == '':
                c = float(left_side[1])
                discriminant = b * b - 4 * a * c
                if discriminant < 0:
                    return False
                elif discriminant == 0:
                    return -b / (2 * a)
                else:
                    return (-b - math.sqrt(discriminant)) / (2 * a), (-b + math.sqrt(discriminant)) / (2 * a)
            return 0, -b / a
        else:
            c = float(left_side[1])
            if c > 0:
                return False
            return -(math.sqrt(-c / a)), math.sqrt(-c / a)
    else:
        return 0


def main():
    equation = input('Введите квадратное уравнение в стандартной форме (ax^2 + bx + c = 0): ')
    equation = equation.replace(' ', '')
    print(equation)
    p = re.compile('^-?([1-9][0-9]*\\*?)?x\\^2([+-]([1-9][0-9]*\\*?)?x)?([+-][1-9][0-9]*)?=0$')
    if p.fullmatch(equation):
        result = solve_quadratic(equation)
        if result is False:
            print('У указанного уравнения нет вещественных корней.')
        elif type(result) == tuple:
            print(f'Корни уравнения - {result}')
        else:
            print(f'Корень уравнения - {result}')
    else:
        print('Это не квадратное уравнение в стандартном виде.')


if __name__ == '__main__':
    main()
