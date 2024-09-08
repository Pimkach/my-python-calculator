main_cycle = True
num1 = None
result = None

def add(num1, num2):
    """сложение"""
    return num1 + num2

def subtract(num1, num2):
    """вычитание"""
    return num1 - num2

def multiply(num1, num2):
    """умножение"""
    return num1 * num2

def divide(num1, num2):
    """
    деление
    ValueError при попытке деления на ноль
    """
    if num2 == 0:
        raise ValueError("Деление на ноль невозможно")
    return num1 / num2

def power(a, b):
    """возводит в степень"""
    return a ** b

def modulo(a, b):
    """остаток от деления"""
    return a % b

def perform_operation(operator, num1, num2):
    """выполнение арифметической операции"""
    operations = {
        '+': add,
        '-': subtract,
        '*': multiply,
        '/': divide,
        '^': power,
        '%': modulo
    }

    if operator not in operations:
        raise ValueError("Неподдерживаемая операция")

    return operations[operator](num1, num2)

def round_result(result):
    """
    запрашивает, нужно ли округлить результат,
    и если да, то до какого количества знаков после запятой
    """
    while True:
        want_round = input('Хотите задать количество знаков после запятой? Да/Нет: ')
        if want_round.lower() in ['да', 'нет']:
            break
        else:
            print("Пожалуйста, введите 'Да' или 'Нет'.")

    if want_round.lower() == 'да':
        while True:
            try:
                col = int(input('Сколько вы хотите знаков после запятой? Введите цифру: '))
                result = round(result, col)
                return result
            except ValueError:
                print("Пожалуйста, введите целое число.")
    else:
        return result

def get_user_input(prompt, valid_options=None):
    """запрашивает ввод и проверяет его корректность"""
    while True:
        user_input = input(prompt)
        if valid_options is None:
            try:
                return float(user_input)
            except ValueError:
                print("Некорректный ввод. Пожалуйста, введите число.")
        elif user_input in valid_options:
            return user_input
        else:
            print(f"Некорректный ввод. Допустимые варианты: {', '.join(valid_options)}")


while main_cycle:

    if num1 is None:
        num1 = get_user_input("Введите первое число: ")

    print('''Доступные операции:
          сложение; вычитание; умножение; деление; возведение в степень; вычисление остатка от деления.''')

    try:
        operator = get_user_input("Выберите операцию (+ - * / ^ %): ", ['+', '-', '*', '/', '^', '%'])

        num2 = get_user_input("Введите второе число: ")

        result = perform_operation(operator, num1, num2)
        rounded_result = round_result(result)
        print(rounded_result)

        answer = get_user_input("Хотите продолжить вычисления с полученным результатом? (+/-): ", ['+', '-'])

        if answer.lower() == '+':
            num1 = rounded_result
        elif answer.lower() == '-':
            num1 = None
    except ValueError as e:
        print(f"Ошибка: {e}")
        num1 = None


    answer = get_user_input("Хотите продолжить или выйти из программы? (+/-): ", ['+', '-'])

    if answer == '-':
        main_cycle = False