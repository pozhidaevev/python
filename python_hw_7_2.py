from abc import ABC, abstractmethod

class CountMaterial(ABC):
    @abstractmethod
    def count_material(self):
        pass


class Clothers(CountMaterial):
    def __init__(self, size, height):
        self.size = size
        if size > 14:
            self.size = 14
        elif size < 4:
            self.size = 4
        self.height = height

    def count_material(self):
        coat_count_material = self.size / 6.5 + 0.5
        suit_count_material = 2 * self.height + 0.3
        print(f'Для пошива 1 пальто и 1 костюма заданных размеров нужно {coat_count_material + suit_count_material:.2f} метра ткани')

class Coat(Clothers):
    def __init__(self, size, number_of_coats):
        super().__init__(size, height=0)
        self.number_of_coats = number_of_coats

    def count_material(self):
        coat_count = (self.size / 6.5 + 0.5) * self.number_of_coats
        print(f'На пошив {self.number_of_coats} пальто размером {self.size}, необходимо {coat_count:.2f} метров ткани')


class Suit(Clothers):
    def __init__(self, height, number_of_suits):
        self.height = height
        self.number_of_suits = number_of_suits

    def count_material(self):
        suit_count = (2 * self.height + 0.3) * self.number_of_suits
        print(f'На пошив {self.number_of_suits} костюмов ростовкой {self.height}, необходимо {suit_count:.2f} метров ткани')

a = Clothers(10, 1.85)
a.count_material()
b = Coat(10, 1)
b.count_material()
c = Suit(1.85, 1)
c.count_material()