class Dog():
    """Простая модель собаки"""
    
    def __init__(self, name, age):
        """Инициализирует атрибуты name и age"""
        self.name = name
        self.age = age
    
    
    def sit(self):
        """Садиться по команде"""
        print(f'{self.name} is now sitting.')
    
    
    def roll(self):
        """Катаеться по команде"""
        print(f'{self.name} rolled over!')
        
        
my_dog = Dog('Mario', 5)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()
my_dog.roll()

your_dog = Dog('Hoshi', 6)
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")
your_dog.sit()
your_dog.roll()