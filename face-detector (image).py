import cv2


cascade=cv2.CascadeClassifier("front_face.xml") #Download the front-face.xml file provided in the repository

img=cv2.imread("Path to the image") #Add the image path you want to detect the face for
gray=cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces=cascade.detectMultiScale(gray,
scaleFactor=1.05,
minNeighbors=5)


for w,x,y,z in faces:
    img=cv2.rectangle(img,(w,x),(w+y , x+z),(0,0,255), 3) #Adding rectangle to the face


cv2.imshow("gray",img)
cv2.waitKey(0)
cv2.destroyAllWindows()