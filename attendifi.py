import cv2
import numpy as np
import face_recognition
import dlib

imgElon = face_recognition.load_image_file('imagedesc/elon.jpeg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('imagedesc/elontest.jpeg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)


#Face Detection section
face_location = face_recognition.face_locations(imgElon)[0] #we use zero here cause we are only getting the first element of this



cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)