# a, b, c = 10, 12, 3
a, b, c = 1, -5, 6

d = b ** 2 - 4 * a * c
print('D = ', d)

x1 = (-b + d ** 0.5) / (2 * a)
x2 = (-b - d ** 0.5) / (2 * a)
print(x1, x2)
