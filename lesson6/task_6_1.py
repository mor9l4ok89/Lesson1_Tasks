import time

class TrafficLight:

    def __init__(self, color):
        self.__rgb = color

red = TrafficLight('Red')
yellow = TrafficLight('Yellow')
green = TrafficLight('Green')

print(red._TrafficLight__rgb)
print(yellow._TrafficLight__rgb, time.sleep(int(7)))
print(green._TrafficLight__rgb, time.sleep(int(2)))
print(time.sleep(int(10)))
