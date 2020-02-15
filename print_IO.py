f = open('temp.txt', 'w')
print('Вывод не на экран, а в файл!', file=f)
print('Вывод не на экран, а в файл!', file=f)

print(f.closed)

with open('temp.txt', 'w') as f:
    print('Вывод не на экран, а в файл!', file=f)
    print('Вывод не на экран, а в файл!', file=f)

print(f.closed)

DEBUG = False

import sys

if DEBUG:
    out = sys.stdout
else:
    out = open('print_IO.log', "w")

print('dsfgdfgdf', file=out)
