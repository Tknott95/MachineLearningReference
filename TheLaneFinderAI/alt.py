import cv2 as cv
import numpy as np
feature_params = dict( maxCorners = 100,
                       qualityLevel = 0.3,
                       minDistance = 7,
                       blockSize = 7 )
lk_params = dict( winSize  = (15,15),
                  maxLevel = 2,
                  criteria = (cv.TERM_CRITERIA_EPS | cv.TERM_CRITERIA_COUNT, 10, 0.03))
color = np.random.randint(0,255,(100,3))

                  # image = cv.imread('./lane-finding.jpeg') # 1:07 https://www.youtube.com/watch?v=eLTLtUVuuy4
# image = cv.imread('./lane-finding-alt.jpeg')
avi = cv.VideoCapture('../Utils/Videos/car-driving.avi')
# lane_image = np.copy(image)
ret, old_frame = avi.read()
old_gray = cv.cvtColor(old_frame, cv.COLOR_BGR2GRAY)
p0 = cv.goodFeaturesToTrack(old_gray, mask = None, **feature_params)
mask = np.zeros_like(old_frame)
while(1):
    ret,frame = avi.read()
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    # calculate optical flow
    p1, st, err = cv.calcOpticalFlowPyrLK(old_gray, frame_gray, p0, None, **lk_params)
    good_new = p1[st==1]
    good_old = p0[st==1]
    # draw the tracks
    for i,(new,old) in enumerate(zip(good_new,good_old)):
        a,b = new.ravel()
        c,d = old.ravel()
        mask = cv.line(mask, (a,b),(c,d), color[i].tolist(), 2)
        frame = cv.circle(frame,(a,b),5,color[i].tolist(),-1)
    img = cv.add(frame,mask)
    cv.imshow('frame',img)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break
    # Now update the previous frame and previous points
    old_gray = frame_gray.copy()
    p0 = good_new.reshape(-1,1,2)
cv.destroyAllWindows()
cap.release()

def roi(img, vertices):
    #blank mask:
    mask = np.zeros_like(img)   
    #filling pixels inside the polygon defined by "vertices" with the fill color    
    cv.fillPoly(mask, vertices, 255)
    #returning the image only where mask pixels are nonzero
    masked = cv.bitwise_and(img, mask)
    return masked

def average_slope_intercept(image, lines):
    left_fit = []
    right_fit = []
    for line in lines:
        x1, y1, x2, y2 = line.reshape(4)
        parameters = np.polyfit((x1, x2), (y1, y2))
        print(parameters)

def canny(image):
    original_image = image

    # gray = cv.cvtColor(lane_image, cv.COLOR_RGB2BGR) #converts input img from one color to another
    img_render = cv.Canny(original_image, threshold1=200, threshold2=300)
    img_render = cv.GaussianBlur(canny,(5, 5), 0)

    vertices = np.array([[10,500],[10,300], [300,200], [500,200], [800,300], [800,500]], np.int32)
    img_render = roi(img_render, [vertices])

    return canny

def render_lines(image, lines):
    line_image = np.zeros_like(image) # same dimensions of image yet many pixels are black
    if lines is not None:
        for line in lines:
            print(line) # will print each line as a 2d array containing our line coordinates in the form [[x1,y1,x2,y2]].. specify with location of lines in correlation to image space
            x1, y1, x2, y2 = line.reshape(4) # now we turn into a 1D array here assigning according to value/ 
            cv.line(line_image, (x1, y1), (x2, y2), (255, 0, 0), 10) # imsge, coords, color, thickness
    return line_image

def area_of_interest(image):
    height = image.shape[0]
    polygons = np.array([
        [(350, height), (600, height), (300, 0)]
    ])
    mask = np.zeros_like(image)
    cv.fillPoly(mask, polygons, 255)
    masked_image = cv.bitwise_and(canny, mask)
    return masked_image

canny = canny(image)
# cropped_image = area_of_interest(canny)
# lines = cv.HoughLinesP(cropped_image, 2, np.pi/180, 100, np.array([]), minLineLength=50, maxLineGap=50)
# image = render_lines(image, lines)
# hybrid_image = cv.addWeighted(image, 0.7, line_image, 1, 1)
# # points in hough table represent the theta and row values that are common between a series of points.
# # thresholds are essentially a minimum iteration count
# cv.imshow('result', hybrid_image)
# cv.waitKey(0)
