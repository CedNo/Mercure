#!/usr/bin/env python3

import mysql.connector
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
import time
import datetime

mydb = mysql.connector.connect(
          user="mercure",
          password="MotDePasse",
          host="AdresseIpServer",
          port='PortServer',
          database="mercure"
        )

mycursor = mydb.cursor()
distance = 0
tempStart = time.time()
obstacles = 0
totalVitesse = 0
nbrVitesses = 0
angleMaxX = 0
angleMaxY = 0
vitesseMax = 0

#APPELER APRES UN MESSAGE DE CAMERA 
def camera_callback(message):
    rospy.loginfo('[MESSAGE ' + rospy.get_caller_id() + ']: ' + str(message.data))

    global obstacles

    if(message.data == 'obstacle'):
        obstacles += 1
    
    if(message.data == 'fin'):
        insert()

#APPELER APRES UN MESSAGE DU SONAR 
def sonar_callback(message):
    rospy.loginfo('[MESSAGE ' + rospy.get_caller_id() + ']: ' + str(message.data))

    global obstacles

    if(message.data == 'obstacle'):
        obstacles += 1

#APPELER APRES UN MESSAGE DE ACCELEROMETRE 
def accel_callback(message):
    rospy.loginfo('[MESSAGE ' + rospy.get_caller_id() + ']: ' + str(message.data))

    global totalVitesse
    global nbrVitesses
    global angleMaxX
    global angleMaxY
    global vitesseMax

    totalVitesse += message.data[2]
    nbrVitesses += 1

    if(angleMaxX < message.data[0]):
        angleMaxX = message.data[0]

    if(angleMaxY < message.data[1]):
        angleMaxY = message.data[1]

    if(vitesseMax < message.data[2]):
        vitesseMax = message.data[2]

#APPELER APRES UN MESSAGE DE GESTION 
def gestion_callback(message):
    rospy.loginfo('[MESSAGE ' + rospy.get_caller_id() + ']: ' + str(message.data))
    
    if(message.data == 'fin'):
        insert()

#ATTEND UN MESSAGE
def listener():
    rospy.init_node('bd_lis', anonymous=True)

    rospy.Subscriber('camera', String, camera_callback)
    rospy.Subscriber('sonar', String, sonar_callback)
    rospy.Subscriber('accelerometre', Float32MultiArray, accel_callback)
    rospy.Subscriber('gestion', String, gestion_callback)

    rospy.spin()

#AJOUTE A LA BD
def insert():
    global distance
    global tempStart
    global obstacles
    global totalVitesse
    global nbrVitesses
    global angleMaxX
    global angleMaxY
    global vitesseMax
    tempFin = time.time()
    temps = tempFin - tempStart

    if (nbrVitesses == 0):
        nbrVitesses = 1

    vitesseMoyenne = totalVitesse / nbrVitesses

    dateTrajet = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    sql = "INSERT INTO trajets VALUES (null, %s, %s, %s, %s, %s, %s, %s, %s)"
    val = (distance, temps, obstacles, vitesseMoyenne, vitesseMax, angleMaxY, angleMaxX, dateTrajet)
    mycursor.execute(sql, val)

    mydb.commit()
    print(mycursor.rowcount, "Trajet ajouter.")

    #reset variables
    distance = 0
    tempStart = time.time()
    obstacles = 0
    totalVitesses = 0
    nbrVitesses = 0
    
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
