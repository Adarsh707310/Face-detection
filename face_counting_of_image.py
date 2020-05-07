import cv2
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

direc = "image/"
files = os.listdir(direc)
names = [direc + name for name in files]
print(len(names))
for name in names:
  # read the input image
  img = cv2.imread(name)
  height = img.shape[0]
  weidth = img.shape[1]
  gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces = face_cascade.detectMultiScale(gray,1.1,4)
  print(len(faces))
  
  for (x ,y, w, h) in faces:
    cv2.rectangle(img, (x,y), (x+w,y+h), (255, 0, 0), 3)
    
  factor = 800/weidth
  weidth = weidth*factor
  height = height*factor
  
  imS = cv2.resize(img, ((int)(weidth),(int)(height)))
  cv2.imshow('img',imS)
  cv2.waitKey()
