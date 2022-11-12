from time import sleep

class TrafficLight:

    __color = ['красный', 'желтый', 'зеленый']

    def get__color(self):
        return self.__color

    def running():
        print(f'Горит {TrafficLight.__color[0]} цвет светофора (7 секунд)'), sleep(7)
        print(f'Горит {TrafficLight.__color[1]} цвет светофора (2 секунды)'), sleep(2)
        print(f'Горит {TrafficLight.__color[2]} цвет светофора (5 секунд)'), sleep(5)


time_work = TrafficLight
time_work.running()