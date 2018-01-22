#! /usr/bin/python3

import time
from threading import Thread

def temperature(value, displacement=None):
    if not displacement:
        displacement = (0, 1, 1, 2, -1, -1, -2, 0, -1, -1, -2, 2, 2, 0)
    current = 0;

    while True:
        value += displacement[current]
        current = (current+1)%len(displacement)
        yield value

class TemperatureSensor(Thread):
    def __init__(self, value=0, displacement=None, interval=1,
					on_change=None):
        Thread.__init__(self)

        self.sensor = temperature(value, displacement)
        self.value = value
        self.interval = interval
        self.on_change = on_change

    def measure(self):
        return self.value

    def run(self):  # interval 간격으로 센서 값 갱신
#        try:
            for self.value in self.sensor:
                time.sleep(self.interval)
                if self.on_change:
                    self.on_change(self.value)
#        except:
            print('센서 스레드가 종료합니다.')

if __name__ == '__main__':
    for value in temperature(5):
        print(value)
        time.sleep(1)
