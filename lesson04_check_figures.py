"""
    Контрольная работа

Вариант-1: Прямоугольный треугольник

Написать функцию triangle(a, b) которая выводит на экран
1. надпись в виде вызова функции со значениями её аргументов
2. прямоугольный треугольник из символа '*' со сторонами a (высота) и b (ширина) так, чтобы
2.1. Вершина треугольника содержала один символ '*'
2.2. Основание треугольники содержало ровно b символов '*'


Вариант-2: Прямоугольник

Написать функцию square(a, b) которая выводит на экран
1. надпись в виде вызова функции со значениями её аргументов
2. рамку прямоугольника из символа '*' со сторонами a (высота) и b (ширина)

def square(a, b):
    print(...)
    ...

square(3, 16)

Примеры будут приведены на экране.


Test print of Triangle

    >>> triangle(3, 9)
    triangle(3, 9)
    *
    ****
    *********
    <BLANKLINE>

    >>> triangle(9, 27)
    triangle(9, 27)
    *
    ***
    *******
    **********
    **************
    *****************
    ********************
    ************************
    ***************************
    <BLANKLINE>

    >>> triangle(3, 16)
    triangle(3, 16)
    *
    ********
    ****************
    <BLANKLINE>

Test print of Square

    >>> square(4, 10)
    square(4, 10)
    **********
    *        *
    *        *
    **********
    <BLANKLINE>

    >>> square(9, 27)
    square(9, 27)
    ***************************
    *                         *
    *                         *
    *                         *
    *                         *
    *                         *
    *                         *
    *                         *
    ***************************
    <BLANKLINE>

    >>> square(3, 16)
    square(3, 16)
    ****************
    *              *
    ****************
    <BLANKLINE>

"""


def triangle(h, w):
    print(f'triangle({h}, {w})')
    interval = h - 1
    delta = w / interval
    print('*')
    x = 0
    x += delta
    while x <= w:
        w_ = round(x)
        print('*' * w_)
        x += delta
    print()


def square(h, w):
    print('square(',h, ',', w, ')')
    print('*' * w)
    # for x in range(h-2):
    #     print('*' + ' '*(w-2)  + '*')
    for i in range(1, a - 1):
        print("*", end='')
        print(" " * (b - 2), end='')
        print("*")

    print('*' * w)
    print()

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    triangle(3, 9)
    triangle(9, 27)
    triangle(3, 16)

    square(4, 10)
    square(9, 27)
    square(3, 16)

