
# < >.py 1|2
from __future__ import print_function

import numpy as np
import cv2 as _cv


def draw_flow(img, flow, step=16):
    h, w = img.shape[:2]
    y, x = np.mgrid[step/2:h:step, step/2:w:step].reshape(2,-1).astype(int)
    fx, fy = flow[y,x].T
    lines = np.vstack([x, y, x+fx, y+fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines + 0.5)
    vis = _cv.cvtColor(img, _cv.COLOR_GRAY2BGR)
    _cv.polylines(vis, lines, 0, (0, 255, 0))
    for (x1, y1), (_x2, _y2) in lines:
        _cv.circle(vis, (x1, y1), 1, (0, 255, 0), -1) 
    return vis


def draw_hsv(flow):
    h, w = flow.shape[:2]
    fx, fy = flow[:,:,0], flow[:,:,1]
    ang = np.arctan2(fy, fx) + np.pi
    v = np.sqrt(fx*fx+fy*fy)
    hsv = np.zeros((h, w, 3), np.uint8)
    hsv[...,0] = ang*(180/np.pi/2)
    hsv[...,1] = 255
    hsv[...,2] = np.minimum(v*4, 255)
    bgr = _cv.cvtColor(hsv, _cv.COLOR_HSV2BGR)
    return bgr


def warp_flow(img, flow):
    h, w = flow.shape[:2]
    flow = -flow
    flow[:,:,0] += np.arange(w)
    flow[:,:,1] += np.arange(h)[:,np.newaxis]
    res = _cv.remap(img, flow, None, _cv.INTER_LINEAR)
    return res

if __name__ == '__main__':
    import sys
    print(__doc__)
    try:
        fn = sys.argv[1]
    except IndexError:
        fn = 0

    cam = _cv.VideoCapture('cod.avi')
    frameWidth = int(cam.get(3))
    frameHeight = int(cam.get(4))
    camSize = (frameWidth, frameHeight)
    result = _cv.VideoWriter('cod_finished.avi', 
                         _cv.VideoWriter_fourcc(*'MJPG'),
                         10, camSize)


    ret, prev = cam.read()
    prevgray = _cv.cvtColor(prev, _cv.COLOR_BGR2GRAY)
    show_hsv = False
    show_glitch = False
    cur_glitch = prev.copy()

    while True:
        ret, img = cam.read()
        gray = _cv.cvtColor(img, _cv.COLOR_BGR2GRAY)
        flow = _cv.calcOpticalFlowFarneback(prevgray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
        prevgray = gray
        
        result.write(draw_flow(gray, flow))
        _cv.imshow('flow', draw_flow(gray, flow))
        if show_hsv:
            result.write(draw_hsv(flow))
            _cv.imshow('flow HSV', draw_hsv(flow))
        if show_glitch:
            cur_glitch = warp_flow(cur_glitch, flow)
            result.write(cur_glitch)
            _cv.imshow('glitch', cur_glitch)

        ch = _cv.waitKey(760)
        if ch == 27:
            break
        if ch == ord('1'):
            show_hsv = not show_hsv
            print('HSV flow visualization is', ['off', 'on'][show_hsv])
        if ch == ord('2'):
            show_glitch = not show_glitch
            if show_glitch:
                cur_glitch = img.copy()
            print('glitch is', ['off', 'on'][show_glitch])
    cam.release()
    result.release()
    _cv.destroyAllWindows()

