class TrafficLight:
    colors = ('Красный', 'Жёлтый', 'Зелёный')
    secs = (7, 2, 13)

    def __init__(self):
        self.__color = ''
        self.sec = 0

    def running(self):
        counter = -1
        for col in self.colors:
            self.__color = col
            print(self.__color, end = " - ")
            counter += 1

            for index, s in enumerate(self.secs):
                self.sec = s
                if counter > index:
                    continue
                else:
                    print(f"{self.sec} секунд")
                    break

traf = TrafficLight()
traf.running()
