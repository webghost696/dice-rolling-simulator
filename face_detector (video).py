import cv2
cascade=cv2.CascadeClassifier("front_face.xml")
video=cv2.VideoCapture(0) #Opens the webCam or you can even paste the path to the already recorded video
frames_captured=0

while True:
    frames_captured += 1
    check,frame=video.read()
    
    faces=cascade.detectMultiScale(frame,
    scaleFactor=1.05,
    minNeighbors=5)

    for w,x,y,z in faces:
        final_vid = cv2.rectangle(frame,(w,x),(w+y , x+z),(0,0,255), 3) #Adding a rectangle to the face
    
    cv2.imshow("detecting",final_vid)
    key=cv2.waitKey(1)
    if key==ord('q'): #Closes the camera when you hit the key 'q'
        break


print(f"{frames_captured} frames were captured")
video.release()
cv2.destroyAllWindows()