import cv2
import numpy as np

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
    
global count

def detectedlane1(imageFrame):

    center1= 0
    center2 = 0

    width,height = 640,480

    pts1 = [[30,380],[630,380],[650,180],[80,180]] 
    #[[BasGauche],[BasDroit], [HautDroit], [HautGauche]]
    #[Horizon, Vertical]

    pts2 = [[0, height], [width, height],[width,0], [0,0]]
    #pts2 = [[0, width], [width, height],[height,0], [0,0]]

    target = np.float32(pts1)
    destination = np.float32(pts2)

    # Apply Perspective Transform Algorithm
    matrix = cv2.getPerspectiveTransform(target, destination)
    result = cv2.warpPerspective(frame, matrix, (width,height))
    #cv2.imshow('Result', result)


    # Valide ce qui sera vue par la caméra #####################################################################

    #cv2.line(imageFrame, (pts1[0][0],pts1[0][1]), (pts1[1][0],pts1[1][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (pts1[1][0],pts1[1][1]), (pts1[2][0],pts1[2][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (pts1[2][0],pts1[2][1]), (pts1[3][0],pts1[3][1]), (0, 255, 0), 1)
    #cv2.line(imageFrame, (pts1[3][0], pts1[3][1]),(pts1[0][0], pts1[0][1]), (0, 255, 0), 1)
    
    #cv2.imshow('Main Image Window', imageFrame)
    
    ############################################################################################################
    
    
    #Filtre bleu ############################################################
    hsv_image = cv2.cvtColor(result, cv2.COLOR_BGR2HSV)
    #cv2.imshow('Filter BlueLine', hsv_image)
    
    bleu1 = np.array([90,86,79])
    bleu2 = np.array([112,255,255])
    
    mask = cv2.inRange(hsv_image, bleu1, bleu2)
    
    #cv2.imshow('Mask', mask)
    
    lignes = cv2.Canny(mask,200,400)
    
    height, width = lignes.shape
    mask2 = np.zeros_like(lignes)
    
    #cv2.imshow('Mask2', mask2)
    
    polygon = np.array([[
        (0, height * 1 / 5),
        (width, height * 1 / 5),
        (width, height),
        (0, height),
    ]], np.int32)
    
    cv2.fillPoly(mask2, polygon, 255)
    
    rho = 1 # Précision de 1 pixel
    angle = np.pi / 180
    seuil_min = 10
    segments = cv2.HoughLinesP(mask2, rho, angle, seuil_min, np.array([]), minLineLength=8, maxLineGap = 4)
    
    masks_image = cv2.bitwise_and(lignes, mask2)
    
    threshold = cv2.Canny(masks_image,200,400)
    edges = cv2.Canny(masks_image, 1, 100, apertureSize=3)
    mergedImage = cv2.add(threshold,edges)
    #cv2.imshow('Merged images ', mergedImage)
    
    firstSquareCenters1 = findCenter((pts2[1][0], pts2[1][1]), (pts2[2][0], pts2[2][1]))
    firstSquareCenters2 = findCenter((pts2[3][0], pts2[3][1]), (pts2[0][0], pts2[0][1]))

    #print("Centers:", firstSquareCenters1,firstSquareCenters2)
    cv2.circle (frame, (firstSquareCenters1,firstSquareCenters1),5,(0,0,255),cv2.FILLED)

    cv2.line(result, firstSquareCenters1, firstSquareCenters2, (0, 255, 0), 1)

    mainFrameCenter = findCenter(firstSquareCenters1,firstSquareCenters2)
    lines = cv2.HoughLinesP(mergedImage,1,np.pi/180,10,minLineLength=120,maxLineGap=250)

    centerPoints = []
    left = []
    right = []
    
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
                    right.append((x1, y1))
                    right.append((x2,y2))
                if center1 !=0 and center2 !=0:
                    centroid1 = findCenter(center1,center2)
                    centerPoints.append(centroid1)                   
        centers = minmax_centerPoints(centerPoints,1)
        laneCenters = 0
        mainCenterPosition = 0        
        if centers is not None:
            laneframeCenter = findCenter(centers[0],centers[1])
            #print(mainFrameCenter,laneframeCenter)          
            mainCenterPosition = mainFrameCenter[0] - laneframeCenter[0]            
            cv2.line(result, centers[0], centers[1], [0, 255, 0], 2)
            laneCenters = centers
           # print(centers)
        return [laneCenters,result,mainCenterPosition]
    else:
        print("No Lines")

frame_counter = 0
     
if __name__ == '__main__':
    cap = cv2.VideoCapture(0, cv2.CAP_V4L2)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH,640) # set the width to 320 p
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480) # set the height to 240 p
    #cap.set(10,60)  # Set le Brightness
    count = 0
    speed = 0
    maincenter = 0
    while(cap.isOpened()):
        frame_counter = frame_counter+1
        #print(frame_counter)
        ret, frame = cap.read()
        if ret == True:
            # Display the resulting frame
            laneimage1 = detectedlane1(frame)
            if laneimage1 is not None:
                maincenter = laneimage1[2]
                cv2.putText(laneimage1[1],"Pos="+str(maincenter),(10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0))
                #cv2.imshow('FinalWindow',laneimage1[1])
                #print("Position-> "+str(maincenter))
        else:
            #cv2.imshow('FinalWindow', frame)
            resizeWindow('FinalWindow',570, 480)
            
        print(maincenter)
            
        key = cv2.waitKey(1)
        if key == 27:
            break
        
    cap.release()
    cv2.destroyAllWindows()
    
