import RPi.GPIO as GPIO
from gpiozero import LED
import time

class Sonar:
    
    MAX_DISTANCE = 220          # Variable qui defini la portée maximal du Sonar.

    def __init__(self, led, trigPin, echoPin):
        GPIO.setwarnings(False)
        self.timeOut = self.MAX_DISTANCE*60   # Calcule le timeOut en fonctionne de la distance maximal.
        GPIO.setmode(GPIO.BOARD)
        self.led = led
        self.trigPin = trigPin
        self.echoPin = echoPin
        GPIO.setup(self.trigPin,GPIO.OUT)
        GPIO.setup(self.echoPin,GPIO.IN)


    def pulseIn(self,pin,level,timeOut): # Obtient le temps d'impulsion d'une broche sous timeOut
        t0 = time.time()
        while(GPIO.input(pin) != level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        t0 = time.time()
        while(GPIO.input(pin) == level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0;
        pulseTime = (time.time() - t0)*1000000
        return pulseTime

    def getSonar(self):     # Retourne la distance du Sonar en cm
        GPIO.output(self.trigPin,GPIO.HIGH)      # trigPin output 10us HIGH level
        time.sleep(0.00001)     # 10us
        GPIO.output(self.trigPin,GPIO.LOW) # trigPin output LOW level
        pingTime = self.pulseIn(self.echoPin,GPIO.HIGH,self.timeOut)   # read plus time of echoPin
        distance = pingTime * 340.0 / 2.0 / 10000.0     # Calcule la distance avec la vitesse du son 340 m/s
        return distance




        

            



