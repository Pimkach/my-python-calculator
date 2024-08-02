V = None
A = None
result = None

while V != 'Stop':

    print('''Доступные операции:
          сложение; вычитание; умножение; деление; возведение в степень; вычисление остатка от деления.''')

    while True:
        operator = input('Выберите операцию (+ - * / ^ %): ')
        if operator in ['+', '-', '*', '/', '^', '%']:
            break
        else:
            print("Некорректный оператор. Попробуйте снова.")


    if A is None:
        while True:
            try:
                A = float(input("Введите первое число: "))
                break
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")

    while True:
        try:
            B = float(input("Введите второе число: "))
            break
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите число.")


    if operator == '+':
        result = A + B
    elif operator == '-':
        result = A - B
    elif operator == '*':
        result = A * B
    elif operator == '/':
        if B == 0:
            print('Нельзя делить на ноль. Попробуйте заново')
            continue
        else:
            result = A / B
    elif operator == '^':
        result = A ** B
    elif operator == '%':
        result = A % B

    while True:
        znak = input('Хотите задать количество знаков после запятой? Да/Нет: ')
        if znak.lower() in ['да', 'нет']:
            break
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")

    if znak.lower() == 'да':
        while True:
            try:
                col = int(input('Сколько вы хотите знаков после запятой? Введите цифру: '))
                result = round(result, col)
                break
            except ValueError:
                print("Пожалуйста, введите целое число.")


    print(result)

    while True:
        W = input('Вы хотите продолжить вычисления с полученным результатом? Да/Нет: ')
        if W.lower() in ['да', 'нет']:
            break
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")

    if W.lower() == 'да':
        A = result
    elif W.lower() == 'нет':
        A = None

    while True:
        check = input('Хотите продолжить или выйти из программы? Продолжить/Выйти: ')
        if check.lower() in ['продолжить', 'выйти']:
            break
        else:
            print("Пожалуйста, введите 'Продолжить' или 'Выйти'.")

    if check.lower() == 'выйти':
        V = 'Stop'