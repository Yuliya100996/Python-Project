class Animal:
    alive = True
    fed = False

    def __init__(self, name):
        self.name = name

class Plant:
    edible = False

    def __init__(self, name):
        self.name = name

class Mammal(Animal):

    def eat(self, food):
        self.food = food
        if self.food == Plant.edible:
            self.fed = True
            return f'{self.name} съел {food.name}'
        else:
            self.alive = False
            return f'{self.name} не стал есть {food.name}'

class Predator(Animal):

    def eat(self, food):
        self.food = food
        if self.food == Plant.edible:
            self.fed = True
            return f'{self.name} съел {food.name}'
        else:
            self.alive = False
            return f'{self.name} не стал есть {food.name}'

class Flower(Plant):
    pass

class Fruit(Plant):
    pass



a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1)
a2.eat(p2)
print(a1.alive)
print(a2.fed)
