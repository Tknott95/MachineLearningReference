import cv2
import numpy as np

# image = cv2.imread('./lane-finding.jpeg') # 1:07 https://www.youtube.com/watch?v=eLTLtUVuuy4
image = cv2.imread('./lane-finding-alt.jpeg')

lane_image = np.copy(image)

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2))
        print(parameters)

def canny(image):
    gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2BGR) #converts input img from one color to another
    blur = cv2.GaussianBlur(gray,(5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def render_lines(image, lines):
    line_image = np.zeros_like(image) # same dimensions of image yet many pixels are black
    if lines is not None:
        for line in lines:
            print(line) # will print each line as a 2d array containing our line coordinates in the form [[x1,y1,x2,y2]].. specify with location of lines in correlation to image space
            x1, y1, x2, y2 = line.reshape(4) # now we turn into a 1D array here assigning according to value/ 
            cv2.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10) # imsge, coords, color, thickness
    return line_image

def area_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(350, height), (600, height), (300, 0)]
    ])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(canny, mask)
    return masked_image

canny = canny(lane_image)
cropped_image = area_of_interest(canny)
lines = cv2.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=50, maxLineGap=50)
line_image = render_lines(lane_image, lines)
hybrid_image = cv2.addWeighted(lane_image, 0.7, line_image, 1, 1)
# points in hough table represent the theta and row values that are common between a series of points.
# thresholds are essentially a minimum iteration count
cv2.imshow('result', hybrid_image)
cv2.waitKey(0)
