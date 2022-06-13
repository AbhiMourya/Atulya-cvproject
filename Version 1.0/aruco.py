import cv2
import cv2.aruco as aruco
import numpy as np


def detect_aruco():
    img1 = cv2.imread("Atulya_Opencv\Ha.jpg")
    img2 = cv2.imread("Atulya_Opencv\HaHa.jpg")
    img3 = cv2.imread("Atulya_Opencv\LMAO.jpg")
    img4 = cv2.imread("Atulya_Opencv\XD.jpg")

    lst_img = [img1, img2, img3, img4]
    aruco_dict = {}
    i = 1
    for img in lst_img:
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        arucodetect=aruco.Dictionary_get(aruco.DICT_5X5_50)
        arucoParam=aruco.DetectorParameters_create()
        bbox,ids,rejected=aruco.detectMarkers(gray,arucodetect,parameters=arucoParam)

        tl = int(bbox[0][0][0][0]),int(bbox[0][0][0][1])
        tr = int(bbox[0][0][1][0]),int(bbox[0][0][1][1])
        br = int(bbox[0][0][2][0]),int(bbox[0][0][2][1])
        bl = int(bbox[0][0][3][0]),int(bbox[0][0][3][1])

        aruco_dict[int(ids)]=(np.array([tl,tr,br,bl]),img)
    return aruco_dict

