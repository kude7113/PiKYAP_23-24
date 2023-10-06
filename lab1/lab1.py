import sys


def get_coef(index, prompt):
    '''
    Читаем коэффициент из командной строки или вводим с клавиатуры

    Args:
        index (int): Номер параметра в командной строке
        prompt (str): Приглашение для ввода коэффицента

    Returns:
        float: Коэффициент квадратного уравнения
    '''
    while True:
        try:
            # Пробуем прочитать коэффициент из командной строки
            coef_str = sys.argv[index]
        except:
            # Вводим с клавиатуры
            print(prompt)
            coef_str = input()
        try:
            # Переводим строку в действительное число
            coef = float(coef_str)
            return coef
        except ValueError:
            print("Ошибка: Введите корректное числовое значение коэффициента.")


def solve_quadratic(a, b, c):
    # Вычисляем дискриминант
    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        # Два действительных корня
        x1 = (-b + discriminant ** 0.5) / (2 * a)
        x2 = (-b - discriminant ** 0.5) / (2 * a)
        q = []
        if x1 > 0:
            x11 = x1
            0.5
            x12 = -x1
            0.5
            q.append(x11)
            q.append(x12)
        elif x1 == 0:
            q.append(0)
        if x2 > 0:
            x21 = x2
            0.5
            x22 = -x2
            0.5
            q.append(x21)
            q.append(x22)
        elif x2 == 0:
            q.append(0)
        return q
    elif discriminant == 0:
        q = []
        # Один действительный корень
        x = -b / (2 * a)
        if x > 0:
            x1 = x
            0.5
            x2 = -x
            0.5
            q.append(x1)
            q.append(x2)
        elif x == 0:
            q.append(0)
        return q
    else:
        q = []
        return q


def main():
    # Получаем коэффициенты A, B, C из командной строки или с клавиатуры
    a = get_coef(1, "Введите коэффициент A: ")
    while a == 0:
        a = get_coef(1, "Это не квадратное уравнение! \nВведите еще раз коэффициент А:")
    b = get_coef(2, "Введите коэффициент B: ")
    c = get_coef(3, "Введите коэффициент C: ")

    solutions = solve_quadratic(a, b, c)

    if len(solutions) == 0:
        print("Корней нет")
    else:
        print("Корни: ", end='')
        for i in solutions:
            print(i, end=", ")


# Если сценарий запущен из командной строки
if __name__ == "__main__":
    main()