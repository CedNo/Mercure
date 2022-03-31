import RPi.GPIO as GPIO
import time
import paho.mqtt.client as paho
import threading

GPIO.setmode(GPIO.BOARD)
delai = .1
val = 0 #Valeur du photoresistor
pinRes = 15 # Pin du photoresistor = cable orange
led = 13 #Pin qui contrôle les lumières du véhicule = cable vert
isOpen = False
GPIO.setup(led, GPIO.OUT)
GPIO.output(led, False)

def photoresistor (pinRes):
    ctr = 0


    GPIO.setup(pinRes, GPIO.OUT)
    GPIO.output(pinRes, False)
    time.sleep(delai)


    GPIO.setup(pinRes, GPIO.IN)


    while (GPIO.input(pinRes) == 0):
        ctr += 1

    return ctr

def on_message(client, userdata, message):
    global isOpen
    print(message.payload.decode("utf-8"))
    if message.payload.decode("utf-8") == str("allume"):
        isOpen = True
    if message.payload.decode("utf-8") == str("ferme"):
        isOpen = False

def thread_lum(name):

    try:
        while True:
            global isOpen
            val = photoresistor(pinRes)
            #print(val)
            if (isOpen == True):
                GPIO.output(led, True)
            elif ( val <= 10000 ):
                GPIO.output(led, False)
            elif (val > 20000):
                GPIO.output(led, True)
    except KeyboardInterrupt:
        pass


    

broker = "localhost"
client = paho.Client("client-subscriber")

print("Connect to broker ", broker)
client.connect(broker)

client.subscribe("lumiere")
client.on_message=on_message
x = threading.Thread(target=thread_lum, args=(1,)) 
x.start()
client.loop_forever() 
  

