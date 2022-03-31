#!/usr/bin/env python3

import rospy
import time
import RPi.GPIO as GPIO
import paho.mqtt.client as paho
import Buzzer

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(37, GPIO.OUT)

def on_message(client, userdata, message):

    poutpout = message.payload.decode("utf-8")
    
    if(int(poutpout) == 0):
        print("PoutPout")
        GPIO.output(37, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(37, GPIO.LOW)
    elif(int(poutpout) > 0):
        Buzzer.choixBuzzer(int(poutpout))

broker = "localhost"
client = paho.Client("client-klaxon")

print("Connect to broker ", broker)
client.connect(broker)

client.subscribe("klaxon")
client.on_message=on_message
client.loop_forever()
