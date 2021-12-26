import cv2 as cv
import numpy as np
 
def handler_thresh(x):
    x=1

def main():
    thresh_value = 100 
    cv.namedWindow('motion',cv.WINDOW_NORMAL)
    cv.createTrackbar('Thershold', 'motion', thresh_value, 255, handler_thresh)
    vdofile = '1depthGRAY.avi'
    cap = cv.VideoCapture(vdofile)
    if not cap.isOpened():
        print("Cannot open vdo")
        exit()
    frames = [] 
    while True:
        thresh_value = cv.getTrackbarPos('Thershold','motion')
        ret, frame = cap.read() 
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
        frame = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        frames.append(frame) 
        if(len(frames)>20): 
            del frames [0] 

        ref_frame = 13   
        print(len(frames))
        if(len(frames)>ref_frame+1):
            motion_no_thres = np.abs(frame - frames[ref_frame])
        else:
            motion_no_thres = np.abs(frame - frames[len(frames)-1]) 
        ref,motion = cv.threshold(motion_no_thres,thresh_value,255,cv.THRESH_BINARY)
        cv.imshow('frame', frame)
        cv.imshow('Thershold',motion)
        if cv.waitKey(100) == 27: 
            break
    cap.release()
 
if __name__ == "__main__":
    main()