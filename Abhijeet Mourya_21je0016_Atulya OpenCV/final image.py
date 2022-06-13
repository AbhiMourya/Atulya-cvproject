import cv2
import numpy as np
import detect_figure
import aruco

img = cv2.imread("Atulya_Opencv\CVtask.jpg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.bilateralFilter(img, 15, 75, 75)

aruco_dict = aruco.detect_aruco()
figure_dict = detect_figure.final_dict

# Repeating for each ids
for i in figure_dict:
    pt_aruco = aruco_dict[i][0]  # Corner point of aruco
    pt_figure = figure_dict[i]  # Corner point of shape
    npt_aruco = np.array([[0, 0], [0, 200], [200, 200], [200, 0]])  # New corner point of aruco
    img_aruco = aruco_dict[i][1]

    # Converting aruco to new cropped image
    matrix, _ = cv2.findHomography(pt_aruco, npt_aruco)
    st_aruco = cv2.warpPerspective(img_aruco, matrix, (200, 200))

    # Wrapping cropped aruco image on given shape
    matrix, _ = cv2.findHomography(npt_aruco, pt_figure)
    imgout = cv2.warpPerspective(st_aruco, matrix, (img.shape[1], img.shape[0]))

    # Making values of pixel=0 where aruco is to be pasted
    img = cv2.fillConvexPoly(img, pt_figure, (0, 0, 0))

    mask = np.array(np.zeros(img.shape))
    mask = cv2.fillConvexPoly(mask, pt_aruco, (255, 255, 255))
    thresh = cv2.bitwise_and(imgout, imgout, mask)

    # Adding aruco image and shpe image
    img = img + imgout

cv2.imshow("out", img)

# Saving final image to memory
cv2.imwrite("Final.jpg", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
