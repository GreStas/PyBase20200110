# from oop_cars import (
#     Car,
#     AutoSalon as AvtoSalon,
# )


from oop_cars import *

# import math
# # print(math.pi, '3.1415926...')
# print(math.__str__(), '45')

print('!'*20, 'Начало avtosalon.py')


car1 = Car()
car1.price = 10
car1.color = 'white'

car2 = Car(model_name='Mazda', price=11, color='cyan')
car3 = Car('Toyota', 10, 'white', vin=hex(121243).upper()[2:])

print(car1, car2, car3, sep='\n')
print('=' * 60)

salon1 = AutoSalon('АВТ Бавария')
salon1.append(car1)
salon1.append(car3)
print(salon1)

try:
    print(f"\nПродан автомобиль {str(salon1.sale(10))}\n")
except IndexError as e:
    print(str(e))
else:
    print(salon1)

print(f"Продан автомобиль {str(salon1.sale(1))}")
print(salon1)

salon1.profit += salon1.paint(car2, 'black')
print(car2)
print(salon1)

car = salon1.search(3)
salon1.paint(car, 'green')
print(salon1)

# salon2 = AutoSalon('Соломенский авторынок')
# salon2.append(car2)
# print(salon2)
