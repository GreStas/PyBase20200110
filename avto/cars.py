__all__ = ('Car',)

reg_id = 0


class Car:

    # def __init__(self, price=0.0, color='black', model_name='Ford', vin=''):
    def __init__(self, model_name='Ford', price=0.0, color='black', vin=''):
        self.price = price
        self.color = color
        self.model_name = model_name
        self.vin = vin
        # внутренний учёт уникального идентификатора автомобиля
        global reg_id
        reg_id += 1
        self.id = reg_id

    def __str__(self):
        # return f"{self.__class__.__name__} {self.price} {self.color}"  # не работает как мы хотим
        return f"{self.id}: {self.model_name}(vin={self.vin}) {self.__class__.__name__} {self.price} {self.color}"


class SuperCar(Car):
    pass
