import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
delai = .1
val = 0 #Valeur du photoresistor
pinRes = 7 #Pin du photoresistor
led = 11 #Pin qui contrôle les lumières du véhicule
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



try:
    while True:
        val = photoresistor(pinRes)
        print(val)
        if ( val <= 10000 ):
                GPIO.output(led, False)
        if (val > 20000):
                GPIO.output(led, True)
                
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
