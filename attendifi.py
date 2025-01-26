import cv2
import numpy as np
import face_recognition
import dlib

imgElon = face_recognition.load_image_file('imagedesc/elon.jpeg')
imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)

imgTest = face_recognition.load_image_file('imagedesc/mck.jpeg')
imgTest = cv2.cvtColor(imgTest,cv2.COLOR_BGR2RGB)


#Face Detection section
face_location = face_recognition.face_locations(imgElon)[0] #we use zero here cause we are only getting the first element of this
#Encoding the Detected Face
encodeElon = face_recognition.face_encodings(imgElon)[0]
cv2.rectangle(imgElon, (face_location[3],face_location[0]),(face_location[1],face_location[2]), (255,0,0),2)

#Face Detection section for main image
face_location_test = face_recognition.face_locations(imgTest)[0]
encodeTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (face_location_test[3],face_location_test[0]),(face_location_test[1],face_location_test[2]), (255,0,0),2)

#linear svm will be used to find out if they match or not
results = face_recognition.compare_faces([encodeElon], encodeTest)

#finding the best match through the distance of the face the lower the distance the better
faceDis = face_recognition.face_distance([encodeElon],encodeTest)
print(results, faceDis)
cv2.putText(imgTest, f'{results} {round(faceDis[0], 2)}', (50,50),cv2.FONT_HERSHEY_COMPLEX,1,(0,0,255),2)

cv2.imshow('Elon Musk', imgElon)
cv2.imshow('Elon Test', imgTest)
cv2.waitKey(0)