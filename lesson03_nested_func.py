def divide(x, y, printing=False):
    def print_result(val):
        if printing:
            if val is None:
                print('Деление на 0 запрещено!')
            else:
                print('Результат деления =', val)

    if y == 0:
        result = None
    elif isinstance(x, int) and isinstance(y, int):
        result = x // y
        print_result(result)
    else:
        result = x / y
        print_result(result)
    return result


printing = True

print(divide(5, 2))
divide(5, 2, True)
divide(5, 2, printing=True)
print(divide(1, 0))
divide(1, 0, True)
