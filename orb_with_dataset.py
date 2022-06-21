from sys import flags
import cv2, numpy as np
import os

image_dir = os.listdir("/Users/yavuzyalcin/Desktop/orbImages")
#print(image_dir)
del image_dir[0]
#print(image_dir)
number_of_images = len(image_dir)
#print(number_of_images)

#img1 = cv2.imread('/Users/yavuzyalcin/Desktop/orb_book 2.jpg',)  #img1 is our reference image frame. 

img1 = None

win_name = 'Camera Matching'
font = cv2.FONT_HERSHEY_SIMPLEX
org = (10, 30)
fontScale = 1
color = (255, 0, 0)
thickness = 2
acc = 0
accuracy_arr = [0] * 5
MIN_MATCH = 10
# ORB Algorithm
detector = cv2.ORB_create(1000)
# Flann Method
FLANN_INDEX_LSH = 6
index_params= dict(algorithm = FLANN_INDEX_LSH,
                   table_number = 6,
                   key_size = 12,
                   multi_probe_level = 1)
search_params=dict(checks=32)
matcher = cv2.FlannBasedMatcher(index_params, search_params)
# To be able to do the real-time camera capture
cap = cv2.VideoCapture(0)              
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cap.isOpened():       
    ret, frame = cap.read() 
    for i in range(number_of_images):
        #print("i = " + str(i))
        img_path = "/Users/yavuzyalcin/Desktop/orbImages/" + str(image_dir[i])
        #print(img_path)
        img1 = cv2.imread(img_path)
        if img1 is None:  # If there is no image selected for matching, just display the current frame
            res = frame
        else:             # If a reference image has been selected
            img2 = frame
            gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
            gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
            # Main feature detection part
            kp1, desc1 = detector.detectAndCompute(gray1, None)
            kp2, desc2 = detector.detectAndCompute(gray2, None)
            # k=2로 knnMatch
            try: matches = matcher.knnMatch(desc1, desc2, 2)
            except: continue
            # Only show if match ratio is over the defined value
            ratio = 0.75
            good_matches = [m[0] for m in matches \
                                if len(m) == 2 and m[0].distance < m[1].distance * ratio]
            #print('good matches:%d/%d' %(len(good_matches),len(matches)))
            matchesMask = np.zeros(len(good_matches)).tolist()
            if len(good_matches) > MIN_MATCH: 
                src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ])
                dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ])
                mtrx, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 4.0)
                #print("mas sum: " + str(mask.sum()))
                accuracy=float(mask.sum()) / mask.size
                accuracy_arr[i] = accuracy
                #acc = accuracy
                #print("accuracy: %d/%d(%.2f%%)"% (mask.sum(), mask.size, accuracy))

    max_value = max(accuracy_arr) 

    if max_value > 0.65:

        max_index = accuracy_arr.index(max_value) 
        acc = max_value
        img_path1 = "/Users/yavuzyalcin/Desktop/orbImages/" + str(image_dir[max_index])
        img1 = cv2.imread(img_path1)

        #print(img_path1)

        img2 = frame
        gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
        gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
        # Main feature detection part
        kp1, desc1 = detector.detectAndCompute(gray1, None)
        kp2, desc2 = detector.detectAndCompute(gray2, None)
        # k=2로 knnMatch
        matches = matcher.knnMatch(desc1, desc2, 2)
        # Only show if match ratio is over the defined value
        ratio = 0.75
        good_matches = [m[0] for m in matches \
                            if len(m) == 2 and m[0].distance < m[1].distance * ratio]
        #print('good matches:%d/%d' %(len(good_matches),len(matches)))
        matchesMask = np.zeros(len(good_matches)).tolist()
        if len(good_matches) > MIN_MATCH: 
            src_pts = np.float32([ kp1[m.queryIdx].pt for m in good_matches ])
            dst_pts = np.float32([ kp2[m.trainIdx].pt for m in good_matches ])
            mtrx, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 4.0)
            accuracy=float(mask.sum()) / mask.size
            accuracy_arr.append(accuracy)
                    #acc = accuracy
                    #print("accuracy: %d/%d(%.2f%%)"% (mask.sum(), mask.size, accuracy))
            if mask.sum() > MIN_MATCH:  
                matchesMask = mask.ravel().tolist()
                h,w, = img1.shape[:2]
                pts = np.float32([ [[0,0]],[[0,h-1]],[[w-1,h-1]],[[w-1,0]] ])
                dst = cv2.perspectiveTransform(pts,mtrx)
                img2 = cv2.polylines(img2,[np.int32(dst)],True,255,3, cv2.LINE_AA)

        res = cv2.drawMatches(img1, kp1, img2, kp2, good_matches, None, flags = cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

        percentage = "{:.2f}".format(acc * 100)
        image = cv2.putText(res, 'Match Percent: ' + str(percentage) + '%', org, font, fontScale, color, thickness, cv2.LINE_AA)

        #imSized = cv2.resize(image, (848, 480))  
        cv2.imshow('ORB Matching', image)
        # Using cv2.putText() method
        key = cv2.waitKey(1)
        if key == 27:    # Esc click will stop the execution
                break          
        elif key == ord(' '): 
            x,y,w,h = cv2.selectROI(win_name, frame, False)
            if w and h:
                img1 = frame[y:y+h, x:x+w]

    else:
        res = frame
        cv2.imshow('ORB Matching', res)
        # Using cv2.putText() method
        key = cv2.waitKey(1)
        if key == 27:    # Esc click will stop the execution
                break          
        elif key == ord(' '): 
            x,y,w,h = cv2.selectROI(win_name, frame, False)
            if w and h:
                img1 = frame[y:y+h, x:x+w]

    accuracy_arr = [0] * 5
    acc = 0

else:
    print("Can't open camera.")
cap.release()                          
cv2.destroyAllWindows()