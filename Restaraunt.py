class Restaraunt():
    """Описывает имя ресторана и тип кухни"""
    
    def __init__(self, restaraunt_name, cuisine_type, location=None):
        """Инициализирует атрибуты restaraunt_name и cuisine_type"""
        self.restaraunt_name = restaraunt_name
        self.cuisine_type = cuisine_type
        self.location = location
        self.quantity_res = 0
    
    
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
    
    def number_served(self):
        print(self.quantity_res) 
    
    def update_number_served(self, quantity):
        self.quantity_res += quantity


res_1 = Restaraunt('homeworks', 'совмещенная')
res_1.open_restaraunt()
res_1.describe_restaraunt()

res_2 = Restaraunt('бражник', 'крутая', 'ул. Ленина, 18, Санкт-Петербург, 197198')
res_2.open_restaraunt()
res_2.describe_restaraunt()
res_2.update_number_served(24)
res_2.number_served()