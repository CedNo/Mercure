#!/usr/bin/env python3

import rospy
import RPi.GPIO as GPIO
import time
from std_msgs.msg import Float64
import paho.mqtt.client as paho

broker = "localhost"
client = paho.Client("sonar-publisher")

class Sonar:
    
    MAX_DISTANCE = 100          # Variable qui defini la portée maximal du Sonar.

    def __init__(self, trigPin, echoPin):
        GPIO.setwarnings(False)
        self.timeOut = self.MAX_DISTANCE*60   # Calcule le timeOut en fonctionne de la distance maximal.
        GPIO.setmode(GPIO.BOARD)
        self.trigPin = trigPin
        self.echoPin = echoPin
        GPIO.setup(self.trigPin,GPIO.OUT)
        GPIO.setup(self.echoPin,GPIO.IN)


    def pulseIn(self,pin,level,timeOut): # Obtient le temps d'impulsion d'une pin sous timeOut
        t0 = time.time()
        while(GPIO.input(pin) != level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0
        t0 = time.time()
        while(GPIO.input(pin) == level):
            if((time.time() - t0) > timeOut*0.000001):
                return 0
        pulseTime = (time.time() - t0)*1000000
        return pulseTime

    def getSonar(self):     # Retourne la distance du Sonar en cm
        GPIO.output(self.trigPin,GPIO.HIGH)      # trigPin output 10us HIGH level
        time.sleep(0.00001)     # 10us
        GPIO.output(self.trigPin,GPIO.LOW) # trigPin output LOW level
        pingTime = self.pulseIn(self.echoPin,GPIO.HIGH,self.timeOut)   # read plus time of echoPin
        distance = pingTime * 340.0 / 2.0 / 10000.0     # Calcule la distance avec la vitesse du son 340 m/s
        return distance

    def msgSonar(self):
        pub = rospy.Publisher('/sonar', Float64, queue_size=10)
        rospy.init_node('sonar_pub', anonymous=True)
        rate = rospy.Rate(10) # 10hz

        while not rospy.is_shutdown():

            distance = self.getSonar()
 #           rospy.loginfo(distance)
            pub.publish(distance)
            strDist = str(distance)
            client.publish("sonar", strDist)
            rate.sleep()

if __name__ == '__main__':
    try:

        print("Connecting to broker...")
        client.connect(broker)

        sonar = Sonar(8, 10)
        sonar.msgSonar()

    except rospy.ROSInterruptException:
        pass