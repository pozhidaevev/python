class Stationery():

    title = ['ручкой', 'карандашом', 'маркером']

    def draw(self):
        print(f'Запуск отрисовки')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {Stationery.title[0]}')


class Pensil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {Stationery.title[1]}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {Stationery.title[2]}')

a = Pen()
a.draw()
b = Pensil()
b.draw()
c = Handle()
c.draw()
d = Stationery()
d.draw()