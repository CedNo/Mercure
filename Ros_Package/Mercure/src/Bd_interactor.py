#!/usr/bin/env python3

import mysql.connector
import rospy
from std_msgs.msg import String
from std_msgs.msg import Float32MultiArray
from std_msgs.msg import Float64
import time
import datetime

mydb = mysql.connector.connect(
          user="User",
          password="Password",
          host="AdresseIp",
          port=Port,
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
isSameObstacle = False

#APPELER APRES UN MESSAGE DE CAMERA 
def camera_callback(message):
    #rospy.loginfo('[MESSAGE ' + rospy.get_caller_id() + ']: ' + str(message.data))
    
    if(message.data == 'fin'):
        insert()

#APPELER APRES UN MESSAGE DU SONAR 
def sonar_callback(message):
    #rospy.loginfo('[MESSAGE ' + rospy.get_caller_id() + ']: ' + str(message.data))
    distance = float(message.data)

    global obstacles
    global isSameObstacle

    if(distance < 15.0 and distance != 0.0 and isSameObstacle == False):
        obstacles += 1
        isSameObstacle = True
    else:
        isSameObstacle = False

#APPELER APRES UN MESSAGE DE ACCELEROMETRE 
def accel_callback(message):
    #rospy.loginfo('[MESSAGE ' + rospy.get_caller_id() + ']: ' + str(message.data))

    global totalVitesse
    global nbrVitesses
    global angleMaxX
    global angleMaxY
    global vitesseMax

    totalVitesse += message.data[2]
    nbrVitesses += 1

    angleX = message.data[0] * 100
    angleY = message.data[1] * 100
    vitesse = message.data[2]

    if(float(angleMaxX) < angleX):
        angleMaxX = angleX

    if(float(angleMaxY) < angleY):
        angleMaxY = angleY

    if(float(vitesseMax) < vitesse):
        vitesseMax = vitesse

#ATTEND UN MESSAGE
def listener():
    rospy.init_node('bd_lis', anonymous=True)

    rospy.Subscriber('camera', String, camera_callback)
    rospy.Subscriber('sonar', Float64, sonar_callback)
    rospy.Subscriber('accelerometre', Float32MultiArray, accel_callback)

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

    vitesseMoyenne = "{:.2f}".format(totalVitesse / nbrVitesses)
    vitesseMax = "{:.2f}".format(vitesseMax)
    distance = "{:.2f}".format(float(vitesseMoyenne) * float(temps) * float(0.278))
    angleMaxX = "{:.2f}".format(angleMaxX)
    angleMaxY = "{:.2f}".format(angleMaxY)

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
    angleMaxX = 0
    angleMaxY = 0
    vitesseMax = 0
    isSameObstacle = False
    
if __name__ == '__main__':
    try:
        listener()
    except rospy.ROSInterruptException:
        pass
