import cv2
import numpy as np
import face_recognition
import dlib
import os
from datetime import datetime

path = 'imagedesc'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])# we dont want to append the extension to
print(classNames)

def findEncodings(images):
    # alist that has the images encodings at the end
    encodeList=[]
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markAttendance(name):
    with open('Attendance.csv','r+') as f:
        myDatabase = f.readlines()
        nameList = []
        for line in myDatabase:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dateStr = now.strftime('%H:%M:%S')
            f.writelines(f'\n {name}, {dateStr}')
        print(myDatabase)



encodeListKnown = findEncodings(images)
print('Encoding Complete.......')

#finding the mtches between out images and the images in the webcan

#setting up a webcam
cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    #reducing the size of image to reduce the process
    imgsmall = cv2.resize(img,(0,0),None,0.25,0.25)
    #convert it to rgb
    imgsmall = cv2.cvtColor(imgsmall, cv2.COLOR_BGR2RGB)
    facesOurFrame = face_recognition.face_locations(imgsmall)
    #finding the encoding of our webcam
    encodeOurFrame = face_recognition.face_encodings(imgsmall,facesOurFrame)

    #iterating throguh all the faces we ahve found and compare them with all the encidings we have\
    for encodeFace, faceLoc in zip(encodeOurFrame, facesOurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = classNames[matchIndex].upper()
            # print(name)

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 9), 2)
            cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            markAttendance(name)
    cv2.imshow('Webcam', img)
    cv2.waitKey(1)
# face_location_test = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (face_location_test[3],face_location_test[0]),(face_location_test[1],face_location_test[2]), (255,0,0),2)
#
# #linear svm will be used to find out if they match or not
# results = face_recognition.compare_faces([encodeElon], encodeTest)
#
# #finding the best match through the distance of the face the lower the distance the better
# faceDis = face_recognition.face_distance([encodeElon],encodeTest)