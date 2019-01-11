import gc


class Car(object):
    def __init__(self, model, price):
        self.model = model
        self.price = price


    @staticmethod
    def get_average_price():
        car_prices = []
        for var in gc.get_objects():
            if isinstance(var, Car):
                car_prices.append(var.price)
        return sum(car_prices)//len(car_prices)


    @classmethod
    def define_euro_standards_for_cars(cls, standarts):
        cls.euro_standarts = standarts


def create_cars_and_count_average_price():
    print('Average price of car will be counted via static method.')

    toyota = Car('Toyota Corolla', 15000)
    audi = Car('Audi A6', 18000)
    nissan = Car('Nissan Almera', 14500)

    print(f'Average price: {Car.get_average_price()}')


def set_euro_standarts_for_cars():
    standarts = 'Euro6'
    print(f'Just now following standarts will be defined for all cars:\n{standarts}')

    Car.define_euro_standards_for_cars(standarts)

    print(f'Now the "Car" entity has an class-attribute "euro_standarts": {Car.euro_standarts}')