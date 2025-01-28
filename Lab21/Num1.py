from Transport import Transport

track = False
flag = True

while flag:
    try:
        trNum = int(input('Выберите вид транспорта: 1 - Машина 2 - Грузовик 3 - Самолет 4 - Поезд 5 - Лодка 6 - Автобус -1 - Выход из программы'))
        try:
            tp = Transport.get_by_index(trNum-1)
            print(tp.get_message())
            if tp == Transport.TRACK:
                track = True
            flag = False
        except IndexError:
            print('Выбрано некорректное значение, выберите из предложенных вариантов')
    except ValueError:
        print('Введено некорректное значение')

if not track:
    flag = True
    ans = input('Желаете ли вы расчитать стоимость поездки ? y - да, n -  нет')
    while flag:
        if ans == 'y':
            try:
                km = int(input('Введите расстояние:'))
                print(f'Стоимость поездки: {tp.get_cost() * km}')
            except ValueError:
                print('Введено некорректное значение')
                continue
        flag = False
