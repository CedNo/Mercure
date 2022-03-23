import RPi.GPIO as GPIO
import pigpio
from time import sleep
from gpiozero import AngularServo
from gpiozero.pins.pigpio import PiGPIOFactory

in1 = 24
in2 = 23
ena = 25
servo = 12

factory = PiGPIOFactory()

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)





#Set les pins en OUT
GPIO.setup(in1, GPIO.OUT)
GPIO.setup(in2, GPIO.OUT)

servo = AngularServo(servo, pin_factory=factory, min_pulse_width=0.0006, max_pulse_width=0.0023)

GPIO.setup(ena, GPIO.OUT)



#GPIO.LOW sur les deux pins = moteur a off / GPIO.HIGH sur une des pins(in1 ou in2) fait tourner le moteur dans une direction
GPIO.output(in1, GPIO.LOW)
GPIO.output(in2, GPIO.LOW)
p1 = GPIO.PWM(ena, 1000)
p1.start(50)



def reset():
    servo.angle = -25


def frontright():
    servo.angle = -80

def frontleft():
    servo.angle = 45



def avancer(speed=50,time=0):
    p1.ChangeDutyCycle(speed)
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.HIGH)
    reset()
    sleep(time)


def reculer(speed=50,time=0):

    p1.ChangeDutyCycle(speed)
    GPIO.output(in1, GPIO.HIGH)
    GPIO.output(in2, GPIO.LOW)
    reset()
    sleep(time)

def stop(time=0):
    GPIO.output(in1, GPIO.LOW)
    GPIO.output(in2, GPIO.LOW)
    sleep(time)

def avDroit(speed=50,time=0):
    avancer(speed)
    frontright()

    sleep(time)

def avGauche(speed=50,time=0):
    avancer(speed)
    frontleft()

    sleep(time)

def arDroit(speed=50,time=0):
    reculer(speed)
    frontright()

    sleep(time)

def arGauche(speed=50,time=0):
    reculer(speed)
    frontleft()
    sleep(time)



