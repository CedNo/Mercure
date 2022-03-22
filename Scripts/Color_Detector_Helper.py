import cv2
import numpy as np

#Ici on va chercher la camera et on la stock dans la variable cap
cap = cv2.VideoCapture(0, cv2.CAP_V4L)
#Taille de l'image
cap.set(3,640)
cap.set(4,480)


def nothing(x):
    pass

cv2.namedWindow("Detection couleur")


#(HSV en anglais pour hue, saturation, value) : Teinte, Saturation, Brillance
#Creation des trackbar
cv2.createTrackbar("LowH", "Detection couleur", 0, 255, nothing)
cv2.createTrackbar("LowS", "Detection couleur", 0, 255, nothing)
cv2.createTrackbar("LowV", "Detection couleur", 0, 255, nothing)
cv2.createTrackbar("UpH", "Detection couleur", 0, 255, nothing)
cv2.createTrackbar("UpS", "Detection couleur", 0, 255, nothing)
cv2.createTrackbar("UpV", "Detection couleur", 0, 255, nothing)
 
while True:
    
    #Ici on lit chaque img de la camera et on le stock dans la variable img
    _,img = cap.read()
    
    #Convertie l'image en hsv pour faire la detection de couleur
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    #Ici avec les trackbar on va chercher notre couleur min et max qu'on veut détecter
    lower_h = cv2.getTrackbarPos("LowH", "Detection couleur")
    lower_s = cv2.getTrackbarPos("LowS", "Detection couleur")
    lower_v = cv2.getTrackbarPos("LowV", "Detection couleur")

    upper_h = cv2.getTrackbarPos("UpH", "Detection couleur")
    upper_s = cv2.getTrackbarPos("UpS", "Detection couleur")
    upper_v = cv2.getTrackbarPos("UpV", "Detection couleur")
    
    #On créer un array avec nos valeurs hsv de la trackbar pour la couleur min et max
    low_HSV = np.array([lower_h, lower_s, lower_v])
    up_HSV = np.array([upper_h, upper_s, upper_v])
    
    #On défini notre mask
    mask = cv2.inRange(hsv, low_HSV, up_HSV)
    
    
    #Ici on va filtrer les images avec notre mask
    result = cv2.bitwise_and(img, img, mask=mask)

    
    cv2.imshow("Video_normal", img)
    cv2.imshow("Video_mask", mask)
    cv2.imshow("Resultat", result)

    key = cv2.waitKey(25) &0xFF
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
