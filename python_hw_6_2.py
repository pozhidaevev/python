class Road:

    __mass_1_m2 = 25 # масса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 см, в килограммах
    __thickness = 5  # число см толщины полотна

    def __init__(self, length, width):
        self._length = length         # длина дороги в метрах
        self._width = width           # ширина дороги в метрах

    def count_mass(self):
        res = self._length * self._width * Road.__mass_1_m2 * Road.__thickness / 1000
        print(f'Для покрытия дороги длиной {self._length} метров и шириной {self._width}'
              f' метров необходимо {res:.3f} тонны асфальта.')


asphalt2 = Road(770, 7)
asphalt2.count_mass()