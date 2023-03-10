class Bird():
    def walk(self):
        print('hoping around')


class Mammal():
    def walk(self):
        print('jogging around')


class Movements:
    @classmethod
    def move(cls, thing):
        thing.walk()


bird = Bird()
dog = Mammal()

Movements.move(bird)
Movements.move(dog)
