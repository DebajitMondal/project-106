import cv2


# Create our body classifier
bodycascad = cv2.CascadeClassifier('haarcascade_fullbody.xml')

# Initiate video capture for video file
cap = cv2.VideoCapture('walking.avi')

# Loop once video is successfully loaded
while True:
    
    # Read first frame
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    #Convert Each Frame into Grayscale
    body = bodycascad.detectMultiScale(gray,1.1,5)
    # Pass frame to our body classifier
    for (x,y,w,h) in body:
       cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
    
    # Extract bounding boxes for any bodies identified
    cv2.imshow("Web cam", frame)


    if cv2.waitKey(1) == 32: #32 is the Space Key
        break

cap.release()
cv2.destroyAllWindows()
