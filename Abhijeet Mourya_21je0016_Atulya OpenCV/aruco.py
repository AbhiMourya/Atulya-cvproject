import cv2
import cv2.aruco as aruco
import numpy as np


# Function to detect aruco ids and corners
def detect_aruco():
    img1 = cv2.imread("Atulya_Opencv\Ha.jpg")
    img2 = cv2.imread("Atulya_Opencv\HaHa.jpg")
    img3 = cv2.imread("Atulya_Opencv\LMAO.jpg")
    img4 = cv2.imread("Atulya_Opencv\XD.jpg")

    lst_img = [img1, img2, img3, img4]
    aruco_dict = {}
    for img in lst_img:
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        arucodetect = aruco.Dictionary_get(aruco.DICT_5X5_50)
        arucoParam = aruco.DetectorParameters_create()
        bbox, ids, rejected = aruco.detectMarkers(gray, arucodetect, parameters=arucoParam)

        # Changing values of corners of aruco to integer
        tl = int(bbox[0][0][0][0]), int(bbox[0][0][0][1])
        tr = int(bbox[0][0][1][0]), int(bbox[0][0][1][1])
        br = int(bbox[0][0][2][0]), int(bbox[0][0][2][1])
        bl = int(bbox[0][0][3][0]), int(bbox[0][0][3][1])

        cv2.imwrite(f"{int(ids)}.jpg", img)

        # Making a dictionary with ids as key and corners as value
        aruco_dict[int(ids)] = (np.array([tl, tr, br, bl]), img)
    return aruco_dict
