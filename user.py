class User():
    """Описывает first_name, last_name и выводит приветсвие каждому пользователю"""
    
    def __init__(self, username, first_name, last_name, age, *info):
        """Инициализирует информацию о пользователе"""
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.info = info
        self.login_attempts = 0
    
    def increment_login_attempts(self):
        """Добавляет + 1 к login_atempts"""
        self.login_attempts += 1
    
    
    def reset_login_atempts(self):
        self.login_attempts = 0
    
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

class Admin(User):
    """Описывает права администратора на основе суперкласса User"""
    
    def __init__(self, username, first_name, last_name, age, *info):
        """Инициализация атрибутов класса"""
        super().__init__(username, first_name, last_name, age, *info)
        self.privileges = Privileges()
        
    
  
class Privileges():
    
    def __init__(self):
        self.privilege = ['-добавление сообщений', '-удаление пользователей', '-выдача банов'] 


    def show_privileges(self):
        """Права администратора"""
        print('---Права администратора---')
        for privileges in self.privilege:
            print(f'-{privileges}')



dachesa = Admin('Dachesa', 'Daniil', 'Chesakov', 18, 'Катаеться на трюковом самокате', 'Любит програмировать', 'Катаеться на сноуборде')
dachesa.privileges.show_privileges()

smolusha = User('smolusha04', 'Maria', 'Smolskаya', 18, 'Прекрасный художник', 'Аниме девочка', 'Суккубчик', 'Милейший человек на свете')
