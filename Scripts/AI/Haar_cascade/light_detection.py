#scripts abandonné ici trop imprécis.
#Fonctionne relativement bien sauf trop de faux positif. Dans notre cas on avait besoin de quelques choses de plus précis.
#J'ai essayer de créer mes propres modèles avec Haarcascade, donc si vous utilisez cette methode vous pouvez utiliser mes modèles. 

import cv2
import numpy as np
import time

import warnings

warnings.filterwarnings("ignore")

cap = cv2.VideoCapture(0, cv2.CAP_V4L)
ctr = 0
ctrStop = 0

while True:
    ret, frame = cap.read()

    if ret == True:

        #Pour trouver les couleur hsv utiliser le color_detector_helper
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower_red1 = np.array([160, 100, 100])
        upper_red1 = np.array([180, 255, 255])
        lower_yellow = np.array([15, 150, 150])
        upper_yellow = np.array([50, 255, 255])
        #lower_red2 = np.array([20, 0, 240])
        #upper_red2 = np.array([80, 10, 255])
        
        
        #mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        maskRouge = cv2.inRange(hsv, lower_red1, upper_red1)
        maskJaune = cv2.inRange(hsv, lower_yellow, upper_yellow)
        #maskr = cv2.add(mask)s
        resRouge = cv2.bitwise_and(frame, frame, mask=maskRouge)
        resJaune = cv2.bitwise_and(frame, frame, mask=maskJaune)

        imgR = cv2.medianBlur(resRouge, 5)
        imgJ = cv2.medianBlur(resJaune, 5)
        ccimgR = cv2.cvtColor(imgR, cv2.COLOR_HSV2BGR)
        cimgR = cv2.cvtColor(ccimgR, cv2.COLOR_BGR2GRAY)

        #Fait la convertion en gray_scale 
        #Fait la convertion en RGB
        img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        img_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        stop_data = cv2.CascadeClassifier('stop_data.xml')

        #Fait la convertion en gray_scale 
        found = stop_data.detectMultiScale(img_gray, 1.5, 3)

        #Regarde combien de stop détecté
        amount_found = len(found)

        #Si on voit des stops
        if amount_found != 0:
            ctrStop += 1
            if ctrStop == 10:
                print("stop!!!!")
                time.sleep(10)
            


        #Si on voit pas de stop on regarde si on voit une lumières rouge (On cherche des cercles rouges)
        else:
            ctrStop = 0
            circlesR = cv2.HoughCircles(cimgR, cv2.HOUGH_GRADIENT, 1, 80, param1=50, param2=10, minRadius=10, maxRadius=30)
            if circlesR is not None:
                ctr += 1
                circlesR = np.uint16(np.around(circlesR))
                for i in circlesR[0, :]:
                    cv2.circle(cimgR, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    cv2.circle(cimgR, (i[0], i[1]), 2, (0, 0, 255), 3)
                print("lumières rouge détecté " + str(ctr))
                
                
            ccimgJ = cv2.cvtColor(imgJ, cv2.COLOR_HSV2BGR)
            cimgJ = cv2.cvtColor(ccimgJ, cv2.COLOR_BGR2GRAY)
            circlesJ = cv2.HoughCircles(cimgJ, cv2.HOUGH_GRADIENT, 1, 80, param1=50, param2=10, minRadius=5, maxRadius=30)
            if circlesJ is not None:
                ctr += 1
                circlesJ = np.uint16(np.around(circlesJ))
                for i in circlesJ[0, :]:
                    cv2.circle(cimgJ, (i[0], i[1]), i[2], (0, 255, 0), 2)
                    cv2.circle(cimgJ, (i[0], i[1]), 2, (0, 0, 255), 3)
                print("lumières jaune détecté " + str(ctr))
            cv2.imshow('', cimgR)
            cv2.imshow('res', resRouge)
    else:
        print("problème avec la caméra")


    

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cv2.destroyAllWindows()