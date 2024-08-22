import cv2
import face_recognition
import pickle
import os

# importing the user images
folderPath = 'images'
PathList = os.listdir(folderPath)
print(PathList)
imgList = []
studentIds = []

for path in PathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    #print(os.path.splitext(path)[0])
    studentIds.append(os.path.splitext(path)[0])
print(studentIds)


def findEncodings(imagelist):
    encodeList = []
    for img in imagelist:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


print("Encoding Started.......")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print("Encoding Complete")


file = open("EncodeFile.p", "wb")
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("file saved")