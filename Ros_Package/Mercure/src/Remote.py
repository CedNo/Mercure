#!/usr/bin/env python3

import rospy
import time
import Motor
import paho.mqtt.client as paho

def on_message(client, userdata, message):
    if message.payload.decode("utf-8") == str("avancer"):
        Motor.avancer(100)
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
        Motor.reculer(100)
        print("reculer")
    elif message.payload.decode("utf-8") == str("stop"):
        Motor.stop()
        Motor.reset()
        print("stop")
    elif message.payload.decode("utf-8") == str("start_auto"):
        Camera.start()
    else:
        Motor.stop()
        Motor.reset()

broker = "localhost"
client = paho.Client("client-remote")

print("Connect to broker ", broker)
client.connect(broker)

client.subscribe("move")
client.on_message=on_message
client.loop_forever()
