# Вычисление факториала числа "по-старинке" с помощью цикла while
x = int(input("Введите целое положительное число: "))
i = 1
fact = 1
while i <= x:
    fact *= i
#     print(str(i) + '! =', fact)
    i += 1
print('----------------------------------')
print(str(x) + '! =', fact)