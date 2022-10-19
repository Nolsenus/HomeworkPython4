import json


def main():
    data = dict({})
    try:
        with open('Task5.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
    except FileNotFoundError:
        open('Task5.json', 'x')
    if 'prefix' not in data.keys():
        data['prefix'] = '/'
    while True:
        command = input('Введите команду: ')
        if command.startswith(data['prefix']):
            command = command.removeprefix(data['prefix'])
            first_space = command.find(' ')
            if first_space == -1:
                first_space = len(command)
            start = command[0:first_space]
            if len(command) == len(start):
                command = ''
            else:
                command = command.removeprefix(start + ' ')
            if start == 'help':
                print('Особые обозначения:')
                print('Угловые скобки(<>) используются для обозначения обязательных аргументов.')
                print('Символы звёздочка(*) по обе стороны используются для обозначения необязательных аргументов.')
                print(f'Список команд(для использования команд, '
                      f'необходимо в начало добавлять префикс {data["prefix"]}, например {data["prefix"]}help):')
                print('add_cat <Название категории>: Добавляет категорию в список категорий.')
                print('add <Название категории>: <Название произведения>--* оценка по 100-бальной шкале*: '
                      'Добавляет произведение в список произведений указанной категории.')
                print('remove_cat <Название категории>: Удаляет указанную категорию из списка категорий.')
                print('remove <Название категории>: <Название произведения>: '
                      'Удаляет указанное произведение из указанной категории')
                print('show_cats: Выводит список категорий.')
                print('show <Название категории>: Выводит спискок произведений указанной категории.')
                print('save: Записывает текущую версию данных в файл.')
                print('discard: Возвращает данные в предыдущее записанное в файл состояние.')
                print('end: Заканчивает работу бота.')
                print('prefix <Новый префикс>: Заменяет префикс команд на указанный.')
                print('help: Выводит информацию по использованию команд бота.')
            elif start == 'add_cat':
                if command in data.keys():
                    print(f'Категория {command} уже есть в списке.')
                else:
                    data[command] = {}
                    print(f'Категория {command} добавлена.')
            elif start == 'add':
                first_semicolon = command.find(':')
                if first_semicolon != -1:
                    category = command[0:first_semicolon]
                    if category in data.keys() and category != 'prefix':
                        command = command.removeprefix(category + ': ')
                        last_dash = command.rfind('--')
                        if last_dash != - 1 and (command.endswith('--') or command[last_dash + 2] == ' '):
                            name = command[0:last_dash]
                            is_new = True
                            is_changing = False
                            if name in data[category]:
                                is_new = False
                                response = input('Указанное название уже есть в списке, '
                                                 'обновить оценку("Да"/Что-либо кроме "Да"):')
                                if response == 'Да':
                                    is_changing = True
                            score = 'Нет оценки'
                            valid_score = True
                            if not command.endswith('--'):
                                try:
                                    num = int(command[last_dash + 3:])
                                    if 0 <= num <= 100:
                                        score = num
                                    else:
                                        valid_score = False
                                        print('Оценка должна быть в промежутке от 0 до 100.')
                                except ValueError:
                                    valid_score = False
                                    print('Оценка должна быть либо целым числом от 0 до 100 либо пустой строкой.')
                            if valid_score:
                                if is_new or is_changing:
                                    data[category][name] = score
                                else:
                                    print(f'Операция отменена, оценка {name} осталась прежней.')
                                if is_new:
                                    print(f'{name} успешно добавлен в {category}, оценка - {score}.')
                                if is_changing:
                                    print(f'Оценка {name} изменена на {score}')
                        else:
                            print('Необходимо заканчивать название суффиксом "--"')
                    elif category == 'prefix':
                        print('prefix - Недопустимое название категории.')
                    else:
                        print(f'Нет категории {category}, чтобы добавить категорию воспользуйтесь командой add_cat')
                else:
                    print('Необходимо заканчивать название категории двоеточием.')
            elif start == 'remove_cat':
                if command in data.keys():
                    del data[command]
                    print(f'Категория {command} удалена.')
                else:
                    print(f'Категории {command} нет в списке категорий.')
            elif start == 'remove':
                first_semicolon = command.find(':')
                if first_semicolon != -1:
                    category = command[0:first_semicolon]
                    if category in data.keys():
                        name = command[first_semicolon + 2:]
                        if name in data[category].keys():
                            del data[category][name]
                            print(f'{name} удалён из категории {category}.')
                        else:
                            print(f'{name} нет в категории {category}')
                    else:
                        print(f'Категории {category} нет в списке категорий.')
                else:
                    print('Необходимо отделять название категории двоеточием на конце.')
            elif start == 'show_cats':
                print(data.keys())
            elif start == 'show':
                if command in data.keys():
                    print(data[command])
                else:
                    print(f'В списке категорий нет категории {command}.')
            elif start == 'save':
                try:
                    with open('Task5.json', 'w', encoding='utf-8') as file:
                        file.write(json.dumps(data, ensure_ascii=False))
                        print('Текущее состояние успешно записано в файл.')
                except IOError:
                    print('Что-то пошло не так.')
            elif start == 'discard':
                response = input('Вы уверены, что хотите восстановить последнее записанное состояние?'
                                 '("Да"/Что-либо кроме"Да"): ')
                if response == 'Да':
                    try:
                        with open('Task5.json', 'r', encoding='utf-8') as file:
                            data = json.load(file)
                            print('Восстановлено последнее записанное состояние.')
                    except IOError:
                        print('Что-то пошло не так.')
                else:
                    print('Операция прервана.')
            elif start == 'end':
                try:
                    with open('Task5.json', 'r', encoding='utf-8') as file:
                        latest_save = json.load(file)
                        if latest_save != data:
                            response = input('У вас есть несохранённые изменения, вы уверены, что хотите выйти?'
                                             '("Да"/Что-либо кроме"Да"): ')
                            if response == 'Да':
                                break
                            else:
                                print('Операция прервана.')
                        else:
                            break
                except IOError:
                    response = input('Не удалось получить последнюю сохранённую версию, вы уверены, что хотите выйти?'
                                     '("Да"/Что-либо кроме "Да"): ')
                    if response == 'Да':
                        break
                    else:
                        print('Операция прервана.')
            elif start == 'prefix':
                if command != '':
                    data['prefix'] = command
                else:
                    print('Вы не указали новый префикс.')
            else:
                print(f'Неизвестная команда, чтобы ознакомиться со списком команд напишите{data["prefix"]}help.')
        else:
            print(f'Комманда должна начинаться с префикса "{data["prefix"]}"')


if __name__ == '__main__':
    main()
