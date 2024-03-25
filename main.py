import paho.mqtt.client as mqtt


def ao_conectar(client, userdata, flags, rc):
    print(f"Nos conectamos com o seguinte código de resultado {rc}")



def ao_receber(client, userdata, msg):
     print(f"{msg.topic} --- {msg.payload}")


cliente = mqtt.Client()

cliente.on_connect = ao_conectar

cliente.on_message=ao_receber

cliente.connect("broker.hivemq.com",1883,60)
cliente.subscribe("aula3a")
cliente.loop_forever()


