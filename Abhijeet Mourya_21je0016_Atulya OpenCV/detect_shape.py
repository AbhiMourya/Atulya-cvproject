import cv2


# Function to get contour of desired shape
def detect_shape(img, shape):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 225, 255, cv2.THRESH_BINARY_INV)
    c, h = cv2.findContours(thresh, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

    for contour in c:
        peri = cv2.arcLength(contour, True)
        approx = cv2.approxPolyDP(contour, 0.01 * peri, True)
        # cv2.drawContours(img,[approx],0,(255,255,0),5)
        sides = len(approx)

        # Returning contour of only desired shape
        if sides == 3 and shape == "triangle":
            return approx
        elif sides == 4:
            x, y, w, h = cv2.boundingRect(approx)
            aspect_ratio = float(w) / h
            # print(aspect_ratio)
            # Checking for squares
            if 0.95 <= aspect_ratio <= 1.05 and (shape == "square" or shape == 'quad'):
                return approx
            elif shape == 'quad':
                return approx
        elif sides == 6 and shape == "hexagon":
            return approx
        elif shape == 'circle':
            return approx
