import time
import Motor
#import CameraC
import paho.mqtt.client as paho

def on_message(client, userdata, message):
    if message.payload.decode("utf-8") == str("avancer"):
        Motor.avancer(80)
        print("Avancer")
    elif message.payload.decode("utf-8") == str("avDroit"):
        Motor.avDroit(90)
        print("avDroit")
    elif message.payload.decode("utf-8") == str("avGauche"):
        Motor.avGauche(90)
        print("avGauche")
    elif message.payload.decode("utf-8") == str("arDroit"):
        Motor.arDroit(90)
        print("arDroit")
    elif message.payload.decode("utf-8") == str("arGauche"):
        Motor.arGauche(90)
        print("arGauche")
    elif message.payload.decode("utf-8") == str("reculer"):
        Motor.reculer(90)
        print("reculer")
    elif message.payload.decode("utf-8") == str("stop"):
        Motor.stop()
        Motor.reset()
        print("stop")
    elif message.payload.decode("utf-8") == str("start_auto"):
        CameraC.start()
    else:
        Motor.stop()
        Motor.reset()

broker = "localhost"
client = paho.Client("client-subscriber")

print("Connect to broker ", broker)
client.connect(broker)

client.subscribe("move")
client.on_message=on_message
client.loop_forever()

print('STOP')