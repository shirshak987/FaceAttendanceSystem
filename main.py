import os

import cv2

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

imageBackground = cv2.imread("resources/backgroundimg.png")

# importing the mode image into list
folderModePath = 'resources/modes'
modePathList = os.listdir(folderModePath)
imgModelList = []
for path in modePathList:
    imgModelList.append(cv2.imread(os.path.join(folderModePath, path)))
    #print(len(imgModelList))

#print(modePathList)


while True:
    success, img = cap.read()

    imageBackground[162:162+480, 55:55+640] = img
    resized_img = cv2.resize(imgModelList[3], (420, 635))

    imageBackground[45:45 + 635, 805:805 + 420] = resized_img
    # cv2.imshow("Webcam", img)
    cv2.imshow("Face Attendance", imageBackground)
    cv2.waitKey(1)