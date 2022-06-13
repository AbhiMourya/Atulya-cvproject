import cv2
import detect_shape
import color_mask

img = cv2.imread("Atulya_Opencv\CVtask.jpg")
img = cv2.resize(img, (0, 0), fx=0.5, fy=0.5)
img = cv2.bilateralFilter(img, 15, 75, 75)


# Function to determine the contour of final image with given color and shape
def figure(img, color, shape='square'):
    colormask = color_mask.colour_mask(img, color)
    contour = detect_shape.detect_shape(colormask, shape)
    return contour


final_dict = {}
# Storing contour with ids in a dictionary
for i in color_mask.colors_dict:
    final_dict[i] = figure(img, color_mask.colors_dict[i], "square")
