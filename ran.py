from random import randint

class Die():
    """Кубик"""
    
    def __init__(self, sides=6):
        self.sides = sides
        
    def roll_die(self):
        if self.sides == 6:
            count = randint(1, 6)
        elif self.sides == 10:
            count = randint(1, 10)
        elif self.sides == 20:
            count = randint(1, 20)
        return count
k = 1
v = 1
b = 1
kubik = Die()
kubik_1 = Die(10)
kubik_2 = Die(20)

print('--6 граней---')
while k <= 10:
    print(f'Попытка - {k}. Результат - {kubik.roll_die()}')
    k += 1

print('---10 граней---')
while v <= 10:
    print(f'Попытка - {k}. Результат - {kubik_1.roll_die()}')
    v += 1

print('---20 граней---')
while b <= 10:
    print(f'Попытка - {k}. Результат - {kubik_2.roll_die()}')
    b += 1