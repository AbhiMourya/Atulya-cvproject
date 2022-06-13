import cv2
import numpy as np

# Ranges of hsv of required colours
black = np.array([[0, 0, 0], [0, 5, 5]])
green = np.array([[40, 140, 200], [50, 180, 255]])
# red=np.array([[0,230,220],[10,255,255]])
peach = np.array([[10, 15, 220], [30, 30, 240]])
orange = np.array([[10, 240, 120], [18, 255, 255]])

colors_dict = {1: green, 2: orange, 3: black, 4: peach}


# Function to give mask of desired color
def colour_mask(img, color):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(img_hsv, color[0], color[1])
    mask = cv2.medianBlur(mask, 5)
    add = np.zeros(img.shape, dtype=np.uint8)
    add[:, :] = [255, 255, 255]
    mask = cv2.cvtColor(mask, cv2.COLOR_BAYER_GB2BGR) + add
    return mask
