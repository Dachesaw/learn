class Restaraunt():
    """Описывает имя ресторана и тип кухни"""
    
    def __init__(self, restaraunt_name, cuisine_type, location=None):
        """Инициализирует атрибуты restaraunt_name и cuisine_type"""
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
        self.location = location
    
    
    def describe_restaraunt(self):
        """Вводит информацию об ресторане"""
        if self.location:
            print(f'Название ресторана - "{self.restaraunt_name.upper()}"')
            print(f'Тип кухни - {self.cuisine_type.title()}')
            print(f'---Где находиться?---')
            print(f'({self.location})')
        else:
            print(f'Название ресторана - "{self.restaraunt_name.upper()}"')
            print(f'Тип кухни - {self.cuisine_type.title()}')
            print(f'---Где находиться?---')
            print(f'Нет адреса')
    
    
    def open_restaraunt(self):
        print(f'\n--- {self.restaraunt_name.upper()} открыт ---')

res_1 = Restaraunt('homeworks', 'совмещенная')
res_1.open_restaraunt()
res_1.describe_restaraunt()

res_2 = Restaraunt('бражник', 'крутая', 'ул. Ленина, 18, Санкт-Петербург, 197198')
res_2.open_restaraunt()
res_2.describe_restaraunt()