class Animal:
    salive = True
    fed = False
    name = name


class Plant:
    edible = False
    name = name


class Mammal(Animal):
    def eat(self, food, edible):
        if self.food == self.edible:
            print(f'{self.name} съел {food.name}')
        elif self.food != self.edible:
            print(f'{self.name} не стал есть {food.name}')


class Predator(Animal):
    def eat(self, food):
        food = food


class Flower(Plant):
    edible = True


class Fruit(Plant):
    edible = True


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
