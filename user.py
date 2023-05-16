class User():
    """Описывает first_name, last_name и выводит приветсвие каждому пользователю"""
    
    def __init__(self, username, first_name, last_name, age, *info):
        """Инициализирует информацию о пользователе"""
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.info = info
        
    
    def user_info(self):
        """Выводит имеющеюся информацию о пользователе"""
        print(f'\nНикнейм - {self.username}')
        print(f'Имя и Фамилия - {self.first_name.title()} {self.last_name.title()}')
        print(f'Возраст - {self.age}')
        if self.info:
            print('---Дополнительная информация---')
            for info in self.info:
                print(info.title())
                
    def greeting_user(self):
        """Выводит индивидуальное приветвие"""
        print(f'Добро пожаловать, {self.first_name.title()} {self.last_name.title()}!')


dachesa = User('Dachesa', 'Daniil', 'Chesakov', 18, 'Катаеться на трюковом самокате', 'Любит програмировать', 'Катаеться на сноуборде')
dachesa.user_info()

smolusha = User('smolusha04', 'Maria', 'Smolskаya', 18, 'Прекрасный художник', 'Аниме девочка', 'Суккубчик', 'Милейший человек на свете')
smolusha.user_info()
dachesa.greeting_user()
smolusha.greeting_user()