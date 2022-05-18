print('Ты можешь загадать любое число на интервале от 0 до числа, которое сам укажешь.')
interval_stop = int(input('Укажи до какого числа будет интервал? - '))
print(f'''\nЗагадывай любое чило от 0 до {interval_stop}.
Я буду пытаться отгадать его, а ты подсказывать больше (>) или меньше (<). Начнем!''')
checklist = list(range(interval_stop + 1))
beginning = 0
end = len(checklist) - 1
while True:
    if beginning <= end:
        middle = int((beginning + end) / 2)
        if beginning == end:
            print(f'Ура, это число -  {middle}. Видишь какой я умный!!')
            break
        answer = input(f'''Это чило {middle}?
        Если да, напишите "=", если загаданное вами число больше напиши "+" и если меньше "-".
        Вашь ответ: ''')
        if answer != '=' or answer != '+' or answer != '-':
            if beginning == end or answer == '=':
                print(f'Ура, это число -  {middle}. Видишь какой я умный!!')
                break
            elif answer == '+':
                beginning = middle + 1
            elif answer == '-':
                end = middle - 1
            else:
                print('''\nГде-то ты допустил ошибку, давай попробуем еще раз!
                        Да - "+", нет - "-".''')
                ans = input('Ответ: ')
                if ans == '+':
                    continue
                else:
                    print('Конец!!')
                    break
        else:
            print('''\nГде-то ты допустил ошибку, давай попробуем еще раз!
            Да - "+", нет - "-".''')
            ans = input('Ответ: ')
            if ans == '+':
                continue
            else:
                print('Конец!!')
                break
    else:
        print('''\nГде-то ты допустил ошибку, давай попробуем еще раз!
         Да - "+", нет - "-".''')
        ans = input('Ответ: ')
        if ans == '+':
            beginning = 0
            end = len(checklist) - 1
            continue
        else:
            print('Конец!!')
            break