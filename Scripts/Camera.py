#!/usr/bin/env python3

import cv2
import numpy as np
import threading
import time
import Motor 
import math

frameImage = None
isStop = True
cntNoLines = 0

ctr = 0
classNames = []
classFile = "/home/pi/Desktop/object_detect/coco.names"
with open(classFile,"rt") as f:
    classNames = f.read().rstrip("\n").split("\n")

configPath = "/home/pi/Desktop/object_detect/ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt"
weightsPath = "/home/pi/Desktop/object_detect/frozen_inference_graph.pb"

net = cv2.dnn_DetectionModel(weightsPath,configPath)
net.setInputSize(320,320)
net.setInputScale(1.0/ 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# Détection des arrêt stop
def getObjects(img, thres, nms, draw=True, objects=[]):
    
    global isStop
    
    classIds, confs, bbox = net.detect(img,confThreshold=thres,nmsThreshold=nms)
    roi = None
    #print(classIds,bbox)
    if len(objects) == 0: objects = classNames
    objectInfo =[]
    if len(classIds) != 0:
        for classId, confidence,box in zip(classIds.flatten(),confs.flatten(),bbox):
            className = classNames[classId - 1]
            if className == "cell phone":
                objectInfo.append([box,className])  
                x, y, w, h = box
                roi = img[y:y+h, x:x+w]
                hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
                lower_red1 = np.array([160, 100, 100])
                upper_red1 = np.array([180, 255, 255])
                maskRouge = cv2.inRange(hsv, lower_red1, upper_red1)
                resRouge = cv2.bitwise_and(roi, roi, mask=maskRouge)
                    
                imgR = cv2.medianBlur(resRouge, 5)
                ccimgR = cv2.cvtColor(imgR, cv2.COLOR_HSV2BGR)
                cimgR = cv2.cvtColor(ccimgR, cv2.COLOR_BGR2GRAY)
                    
                circlesR = cv2.HoughCircles(cimgR, cv2.HOUGH_GRADIENT, 1, 80, param1=50, param2=10, minRadius=0, maxRadius=100)
                if circlesR is not None:
                    global ctr
                    ctr += 1
                    print("lumières rouge détecté " + str(ctr))
                    isStop = False
                else :
                    isStop = True
            if className == "stop sign":
                print("stop")
                isStop = False
                time.sleep(3)
                isStop = True
                time.sleep(10)

def findCenter(p1,p2):
    center = ((p1[0] + p2[0]) // 2, (p1[1] + p2[1]) // 2)
    return center

def minmax_centerPoints(tergetList,pos):
    if len(tergetList) > 0:
        maximum = max(tergetList, key = lambda i: i[pos])
        minimum = min(tergetList, key = lambda i: i[pos])
        return [maximum,minimum]
    else:
        return None

# Détect les lignes au sol
def detectLine(imageFrame):

    global isStop
    global cntNoLines

    center1 = 0
    center2 = 0

    #Dimension de la fenêtre
    width,height = 640, 480

    #Selectionne une partie de l'image qui sera analysé
    #pts1 = [[40,380],[580,380],[580,200],[30,200]]
    pts1 = [[30,380],[630,380],[650,180],[80,180]] 
    #[[BasGauche],[BasDroit], [HautDroit], [HautGauche]]
    #[Horizon, Vertical]

    pts2 = [[0, height], [width, height],[width,0], [0,0]]

    target = np.float32(pts1)
    destination = np.float32(pts2)

    #Applique la perspective
    matrix = cv2.getPerspectiveTransform(target, destination)
    result = cv2.warpPerspective(imageFrame, matrix, (width,height))

    #Applique une filtre de couleur
    hsv_image = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
#    cv2.imshow('Filter BlueLine', hsv_image)

    #Range de couleur a analyser
    bleu1 = np.array([90,86,79])
    bleu2 = np.array([112,255,255])

    #Cree un mask noir et blanc
    mask = cv2.inRange(hsv_image, bleu1, bleu2)
#    cv2.imshow('Mask ', mask)

    # Fait resortir le contour des lignes bleus
    lignes = cv2.Canny(mask,200,400)
    height, width = lignes.shape
    mask2 = np.zeros_like(lignes)
#    cv2.imshow('Mask ', mask)

    polygon = np.array([[
        (0, height * 1 / 5),
        (width, height * 1 / 5),
        (width, height),
        (0, height),
    ]], np.int32)

    cv2.fillPoly(mask2, polygon, 255)
    masks_image = cv2.bitwise_and(lignes, mask2)

    #Detect segment
    rho = 1 # Précision de 1 pixel
    angle = np.pi / 180
    seuil_min = 10
    segments = cv2.HoughLinesP(masks_image, rho, angle, seuil_min, np.array([]), minLineLength=8, maxLineGap = 4)

    threshold = cv2.Canny(masks_image,200,400)
    edges = cv2.Canny(masks_image, 1, 100, apertureSize=3)

    mergedImage = cv2.add(threshold,edges)
    cv2.imshow('Merged images ', mergedImage)

    firstSquareCenters1 = findCenter((pts2[1][0], pts2[1][1]), (pts2[2][0], pts2[2][1]))
    firstSquareCenters2 = findCenter((pts2[3][0], pts2[3][1]), (pts2[0][0], pts2[0][1]))

    cv2.line(result, firstSquareCenters1, firstSquareCenters2, (0, 255, 0), 1)
    mainFrameCenter = findCenter(firstSquareCenters1,firstSquareCenters2)
    lines = cv2.HoughLinesP(mergedImage,1,np.pi/180,10,minLineLength=100,maxLineGap=150)

    centerPoints = []
    left = []
    right = []
    centers = None

    if lines is not None:
        for line in lines:
            x1,y1,x2,y2 = line[0]
            if 0<=x1 <=width and 0<= x2 <=width :
                center = findCenter((x1,y1),(x2,y2))
                if center[0] < (width//2):
                    center1 = center
                    left.append((x1, y1))
                    left.append((x2,y2))
                else:
                    center2 = center
                    right.append((x1*-1, y1*-1))
                    right.append((x2*-1,y2*-1))
                if center1 !=0 and center2 !=0:
                    centroid1 = findCenter(center1,center2)
                    centerPoints.append(centroid1)
        centers = minmax_centerPoints(centerPoints,1)
        laneCenters = 0
        mainCenterPosition = 0
    else:
        cntNoLines = cntNoLines + 1
        if cntNoLines == 10 :
            isStop = False
            Motor.stop()
    if centers is not None:
        laneframeCenter = findCenter(centers[0],centers[1])        
        mainCenterPosition = mainFrameCenter[0] - laneframeCenter[0]            
        cv2.line(result, centers[0], centers[1], [0, 255, 0], 2)
        laneCenters = centers
        return [laneCenters,result,mainCenterPosition]
    else:
        print("No Lines")
        
def threadCamera():
    global frameImage
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) 
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) 
    while(cap.isOpened()):
        ret, frame = cap.read()
        frameImage = frame

def threadLine():
    global frameImage
    frameCounter = 0
    count = 0
    speed = 0
    cntNoLines = 0
    maincenter = 0
    while True :
        frameCounter = frameCounter +1
        laneimage1 = detectLine(frameImage)
        if laneimage1 is not None:
            maincenter = laneimage1[2]
            cv2.putText(laneimage1[1],"Pos="+str(maincenter),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
            #print("Position-> "+str(maincenter))
        
        print(maincenter)
        
        angle = (maincenter - 20) / 3
        
        print(angle)
        
        if angle > -20 :
            angle = (1/7.45) * math.sqrt(abs(angle) + 20) * angle
        else :
            angle = (1/7.45) * math.sqrt(abs(angle) - 20) * angle

        if isStop:
            if maincenter <= 15 and maincenter >= -15:
                Motor.avancer(45)
            elif maincenter > 15 and frameCounter % 2 == 0:
                if angle > 35 :
                    angle = 35
                Motor.avGauche(58 , angle)
            elif maincenter < - 15 and frameCounter % 2 == 0:
                if angle < -58 :
                    angle = -58
                Motor.avDroit(58, angle)
        else:
            Motor.stop()

def threadObject():
    global frameImage
    while True:
        result = getObjects(frameImage,0.25,0.2, objects=['cell phone', 'stop sign'])
    
if __name__ == '__main__':

    thCamera = threading.Thread(target=threadCamera, args=())
    thCamera.daemon = True
    thCamera.start()

    time.sleep(1)

    thObject = threading.Thread(target=threadObject, args=())
    thObject.daemon = True
    thObject.start()

    thLine = threading.Thread(target=threadLine, args=())
    thLine.daemon = True
    thLine.start()
