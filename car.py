class Car():
    """Простой класс автомобиля"""
    
    def __init__(self, make, model, year):
        """Инициализация атрибутов автомобиля"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_describe_name(self):
        long_name = (f'{self.year} {self.make} {self.model}')
        return long_name.title()
    
    def read_odometer(self):
        """Выводит пробег"""
        print(f'Miles - {self.odometer_reading}')
        
    def update_odometer(self, miles):
        if miles >= self.odometer_reading:
            self.odometer_reading = miles
        else:
            print('Нельзя делать пробег меньше чем он есть!!!')
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles
    
    
class Battery():
    """Простая модель аккамулятора автомобиля"""
    
    def __init__(self, battery_size=75):
        """Инициализирует атрибуты электромобиля"""
        self.battery_size = battery_size
        
    def describe_battery(self):
        "Выводит информацию о мощности аккумулятора"
        print(f'Мощность аккумулятора - {self.battery_size}-kWh.')

    def get_range(self):
        """Выводит приблизительный запас хода"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f'Автомобиль проедет {range} километров, при полном заряде.')

    def upgrade_battery(self):
        if self.battery_size < 100:
            self.battery_size = 100


class ElectricCar(Car):
    """Представляет аспекты специфические для электромобилей."""
    
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()


