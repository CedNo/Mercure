import cv2

  
# Ouvre la caméra et defini la taille de l'image
cap = cv2.VideoCapture(0, cv2.CAP_V4L)
cap.set(cv2.CAP_PROP_FRAME_WIDTH,640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,480)





while True:
    _, img = cap.read()
    #Fait la convertion en gray_scale 
    #Fait la convertion en RGB
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cimg = img
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
      
      
    #Classifier .xml
    stop_data = cv2.CascadeClassifier('stop.xml')
    
    
    #(img_converti en gray_scale, scaleVal, Minimum Neighbors)  
    found = stop_data.detectMultiScale(img_gray, 1.1, 3)
      
    # Ne rien faire s'il n'a pas de stop

    amount_found = len(found)
      
    if amount_found != 0:
        print("stop!!!!")
          
        # There may be more than one
        # sign in the image
        for (x, y, width, height) in found:
              
            #fait un rectangle alentour d'un stop
            cv2.rectangle(img_rgb, (x, y), 
                          (x + height, y + width), 
                          (0, 255, 0), 5)
    else:
        print("pas de stop")
        
        
    cv2.imshow("Test", img_rgb)
    k=cv2.waitKey(10)& 0xff
    if k==27:
        break
