import sys
from tkinter import *
from tkinter.ttk import *
from sensor.temperature import TemperatureSensor
import paho.mqtt.client as mqtt
from datetime import datetime

class SensorFrame(Frame):
    def __init__(self, master, category ='', location='', value=0):
        Frame.__init__(self, master)  # master는 부모 윈도우

        self.master = master
        self.master.title('센서 : ' + category)
        self.pack(fill=BOTH, expand=True)  # 부모 윈도우 크기에 맞게 크기 조정

        self.scale = Scale(self, from_=0, to=100, orient=VERTICAL)
        self.scale.pack(ipadx=10, ipady=0, side=LEFT)

        self.lblValue = Label(self, text=str(value))
        self.lblValue.pack(side=LEFT, fill=X, padx=10, expand=True)

        self.sensor = TemperatureSensor(value,
                               on_change=lambda v:self.on_change(v))
        self.sensor.start()
        self.set_value(self.sensor.measure())

        self.location = location
        self.connect()

    def connect(self):
        self.mqttc = mqtt.Client()
        self.connected = False
        self.mqttc.connect('localhost')
        self.mqttc.loop(1)


    def set_value(self, value):
        self.lblValue.config(text="온도 : " + str(value))
        self.scale.set(50-value)


    def on_change(self, value):
        self.set_value(value)

        msg = str(value) + '/' + str(datetime.now())[:19]
        self.mqttc.publish('home/iot/temperature/' + self.location,msg)
        self.mqttc.loop(1)


def main():
    value = 10       # 디폴트 값
    category  = 'temperature'
    location  = 'livingroom'
    if len(sys.argv) > 3 :
        category = sys.argv[1]
        location = sys.argv[2]
        value = int(sys.argv[3])

    root = Tk()								# 메인 윈도우
    root.geometry("200x100+100+100")	# 가로x세로+X위치+Y위치
    SensorFrame(root, category, location, value)
    root.mainloop()

if __name__ == '__main__':
    main()
