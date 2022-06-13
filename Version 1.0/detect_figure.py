import cv2
import detect_shape
import color_mask

img = cv2.imread("Atulya_Opencv\CVtask.jpg")
img = cv2.resize(img, (0,0),fx =0.5, fy = 0.5)
img=cv2.bilateralFilter(img,15,75,75)

def figure(img,color,shape='square'):
    colormask=color_mask.colour_mask(img,color)
    contour= detect_shape.detect_shape(colormask,shape)
    return (contour)

final_dict={}
for i in color_mask.colors_dict:
    final_dict[i]=figure(img,color_mask.colors_dict[i],"square")
