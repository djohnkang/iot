#! /usr/bin/python3
import sys
from tkinter import *
from actor.light import Light
import paho.mqtt.client as mqtt
from datetime import datetime

class LightFrame(Frame):
    def __init__(self, master, category='', location='', value=0):
        Frame.__init__(self, master, bg='black')  # master는 부모 윈도우

        self.master = master
        self.master.title('전등 : ' + category)
        self.pack(fill=BOTH, expand=True)  # 부모 윈도우 크기에 맞게 크기 조정

        # 전등
        self.light = Light(self)
        self.light.pack(side=LEFT, expand=True)

        # 전등 제어 버튼
        self.lightButton = Button(self, text="전등 켜기",
								command=lambda: self.on_light_btn_click())
        self.lightButton.pack(side=LEFT, expand=True)
        self.location = location

        self.connect()

    def connect(self):
        self.mqttc = mqtt.Client()
        self.mqttc.connect('localhost')
        self.mqttc.loop(1)

    def on_light_btn_click(self):
        self.light.status = not self.light.status
        if self.light.status:
            self.turn_on()
        else:
            self.turn_off()

        msg = str(self.light.status) + '/' + str(datetime.now())[:19]
        print(msg)
        self.mqttc.publish('home/iot/light/' + self.location,msg)
        self.mqttc.loop(1)

    def turn_on(self):
        self.light.turn_on()
        self.lightButton.config(text='전등 끄기')
        self.config(bg='white')

    def turn_off(self):
        self.light.turn_off()
        self.lightButton.config(text='전등 켜기')
        self.config(bg='black')


def main():
    root = Tk()								# 메인 윈도우
    root.geometry("300x100+100+100")	# 가로x세로+X위치+Y위치
    location = 'livingroom'       # 디폴트 값

    if len(sys.argv) > 1 :
        location = sys.argv[1]

    app = LightFrame(root, location=location)
    root.mainloop()

if __name__ == '__main__':
    main()
