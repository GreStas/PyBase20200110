from .cars import Car

__all__ = ('AutoSalon', 'Store')

class AutoSalon:
    def __init__(self, name):
        self.name = name
        self.cars = []  # Перечень автомобилей в салоне
        self.profit = 0.0

    def __str__(self):
        result = []
        for car in self.cars:
            result.append(str(car))
        report_of_cars = '\n'.join(result)
        return '\n' + '='*60 + f"\n{self.name} (касса={self.profit}):\n{report_of_cars}\n" + '='*60 + '\n'

    def append(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'Ожидается тип `Car`, а получен {type(car)}')
        self.cars.append(car)

    def search(self, id):
        """
            Найти автомобиль на складе

        :param id: id авто
        :return: экземпляр Car
        """
        for car in self.cars:
            if car.id == id:
                return car
        # raise IndexError

    def sale(self, car_id):
        car = self.search(car_id)
        if not car:
            raise IndexError(f'Автомобиль с индексом {car_id} не найден!')
        self.cars.remove(car)  # car = self.cars.pop(car)
        self.profit += car.price
        return car

    def paint(self, car, color):
        car.color = color
        return 0.5

    def load(self):
        """
            Загрузить днные салона из файла
        """
        # TODO сделать загрузку из файла
        self.append(
            Car(
                model_name='Mazda',
                price=11,
                color='cyan',
            )
        )
        self.append(Car('Toyota', 10, 'white', vin=hex(121243).upper()[2:]))


class Store(AutoSalon):

    def __init__(self, name):
        super().__init__(name)
        self.sold = list()

    def sale(self, car_id):
        car = super().sale(car_id)
        self.sold.append(car)
        return car
