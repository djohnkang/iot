import paho.mqtt.client as mqtt

# 클라이언트가 서버에게서 CONNACK 응답을 받을 때 호출되는 콜백
def on_connect(self, client, userdata, rc):
    print ("Connected with result coe " + str(rc))
    # client.subscribe("hello/world")
    self.subscribe("hello/world")

# 서버에게서 PUBLISH 메시지를 받을 때 호출되는 콜백
def on_message(self, userdata, msg):
    print("Topic: ", msg.topic + '\nMessage: ' + msg.payload.decode())

client = mqtt.Client()			# MQTT Client 오브젝트 생성
client.on_connect = on_connect		# on_connect callback 설정
client.on_message = on_message	# on_message callback 설정

client.connect("localhost", 1883, 60)   # MQTT 서버에 연결

# 네트웍 트래픽을 처리, 콜백 디스패치, 재접속 등을 수행하는 블러킹 함수
# 멀티스레드 인터페이스나 수동 인터페이스를 위한 다른 loop*() 함수도 있음
client.loop_forever()