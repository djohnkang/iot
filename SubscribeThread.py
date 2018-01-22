import paho.mqtt.client as mqtt
from threading import Thread

class SubscribeThread(Thread):
    def __init__(self, topic, handler):
        super().__init__()
        self.topic = topic
        self.handler = handler

        self.client = mqtt.Client()
        self.client.on_connect = lambda *args : self.on_connect(*args)
        self.client.on_message = lambda *args : self.on_message(*args)

    def on_connect(self, client, userdata, flags, rc):
        if rc == 0:
            print('연결 성공')
            # 연결 성공시 토픽 구독 신청
            self.client.subscribe(self.topic)
        else:
            print('연결 실패 :  ', rc)

    def on_message(self, client, userdata, msg):
        self.handler(msg)

    def run(self):
        try:
            self.client.connect("localhost")
            self.client.loop_forever()
            # Thread(target=lambda :
            #         self.client.loop_forever()).start()

        except Exception as err:
            print('에러 : %s' % err)
