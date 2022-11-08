import cv2 as cv
import numpy as np
import glob

image_paths = glob.glob('/Users/Sobhyzz/bsg_AhmedSobhy_C/Photomosaic/Resources/*.png')
images = []
image_paths.sort()
for image in image_paths:
    img = cv.imread(image)
    # img = cv.resize(img, (400,400))
    # img = cv.rotate(img, cv.ROTATE_90_CLOCKWISE)
    images.append(img)

def mix_and_match(leftImage, warpedImage):
	i1y, i1x = leftImage.shape[:2]
	i2y, i2x = warpedImage.shape[:2]
	black_l = np.where(leftImage == np.array([0,0,0]))
	black_wi = np.where(warpedImage == np.array([0,0,0]))
	for i in range(0, i1x):
		for j in range(0, i1y):
			try:
				if(np.array_equal(leftImage[j,i],np.array([0,0,0])) and  np.array_equal(warpedImage[j,i],np.array([0,0,0]))):
					warpedImage[j,i] = [0, 0, 0]
				else:
					if(np.array_equal(warpedImage[j,i],[0,0,0])):
						warpedImage[j,i] = leftImage[j,i]
					else:
						if not np.array_equal(leftImage[j,i], [0,0,0]):
							bw, gw, rw = warpedImage[j,i]
							bl,gl,rl = leftImage[j,i]
							warpedImage[j, i] = [bl,gl,rl]
			except:
				pass
	return warpedImage



a = images[0]
# cv.imshow("l",final)
# cv.waitKey(0)
ver = []
for j in range(4):
    print(j)
    b = images[j]
    a = images[j+4]
    sift = cv.SIFT_create()
    tm1 = cv.cvtColor(a , cv.COLOR_BGR2GRAY)
    tm2 = cv.cvtColor(b, cv.COLOR_BGR2GRAY)
    kp1, des1 = sift.detectAndCompute(tm2,None)
    kp2, des2 = sift.detectAndCompute(tm1,None)

    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)

    good = []
    gooods = []
    for i , (m, n) in enumerate(matches):
    	if m.distance < 0.7*n.distance:
            gooods.append([m])
            good.append((m.trainIdx, m.queryIdx))

    if len(good)<4:
        continue
    
    matchedPointsCurrent = np.float32(
    				[kp1[i].pt for (__, i) in good]
    			)
    matchedPointsPrev = np.float32(
    				[kp2[i].pt for (i, __) in good]
    				)
    H, __ = cv.findHomography(matchedPointsCurrent, matchedPointsPrev, cv.RANSAC, 4)

    img3 = cv.drawMatchesKnn(b,kp1,a,kp2,gooods,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow("lll",img3)
    cv.waitKey()

    xh = np.linalg.inv(H)

    ds = np.dot(xh, np.array([a.shape[1], a.shape[0], 1]))
    ds = ds/ds[-1]

    f1 = np.dot(xh, np.array([0,0,1]))
    f1 = f1/f1[-1]

    xh[0][-1] += abs(f1[0])
    xh[1][-1] += abs(f1[1])
    ds = np.dot(xh, np.array([a.shape[1], a.shape[0], 1]))
    
    offsety = abs(int(f1[1]))
    offsetx = abs(int(f1[0]))
    dsize = (int(ds[0])+offsetx, int(ds[1]) + offsety)

    tmp = cv.warpPerspective(a, xh, dsize)

    tmp[offsety:b.shape[0]+offsety, offsetx:b.shape[1]+offsetx] = b
    a = tmp
    imgray = cv.cvtColor(a, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 127, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cnt = max(contours,key = cv.contourArea)
    x,y,w,h = cv.boundingRect(cnt)
    tmp = a[y:y+h,x:x+w]
    ver.append(tmp)

for j in  range(4):
    ver[j] =cv.resize(ver[j],(ver[0].shape[1],ver[0].shape[0]))
    cv.imshow("lll", ver[j])
    cv.waitKey()
# a = ver[2]
# for b in ver[3:]:
    
#     sift = cv.SIFT_create()
#     tm1 = cv.cvtColor(a , cv.COLOR_BGR2GRAY)
#     tm2 = cv.cvtColor(b, cv.COLOR_BGR2GRAY)
#     kp1, des1 = sift.detectAndCompute(tm2,None)
#     kp2, des2 = sift.detectAndCompute(tm1,None)

#     bf = cv.BFMatcher()
#     matches = bf.knnMatch(des1,des2,k=2)

#     good = []
#     for i , (m, n) in enumerate(matches):
#     	if m.distance < 0.7*n.distance:
#     		good.append((m.trainIdx, m.queryIdx))

#     if len(good)<4:
#         continue
    
#     matchedPointsCurrent = np.float32(
#     				[kp1[i].pt for (__, i) in good]
#     			)
#     matchedPointsPrev = np.float32(
#     				[kp2[i].pt for (i, __) in good]
#     				)
#     H, __ = cv.findHomography(matchedPointsCurrent, matchedPointsPrev, cv.RANSAC, 4)



#     xh = np.linalg.inv(H)

#     ds = np.dot(xh, np.array([a.shape[1], a.shape[0], 1]))
#     ds = ds/ds[-1]

#     f1 = np.dot(xh, np.array([0,0,1]))
#     f1 = f1/f1[-1]

#     xh[0][-1] += abs(f1[0])
#     xh[1][-1] += abs(f1[1])
#     ds = np.dot(xh, np.array([a.shape[1], a.shape[0], 1]))
    
#     offsety = abs(int(f1[1]))
#     offsetx = abs(int(f1[0]))
#     dsize = (int(ds[0])+offsetx, int(ds[1]) + offsety)

#     tmp = cv.warpPerspective(a, xh, dsize)
#     print(tmp.shape)
#     tmp[offsety:b.shape[0]+offsety, offsetx:b.shape[1]+offsetx] = b
#     a = tmp
#     cv.imshow("lll",a)
#     cv.waitKey(0)



leftImage = ver[2]

for each in ver[3:]:
    sift = cv.SIFT_create()
    tm1 = cv.cvtColor(each , cv.COLOR_BGR2GRAY)
    tm2 = cv.cvtColor(leftImage, cv.COLOR_BGR2GRAY)
    kp1, des1 = sift.detectAndCompute(tm2,None)
    kp2, des2 = sift.detectAndCompute(tm1,None)
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)
    good = []
    gooods = []
    for i , (m, n) in enumerate(matches):
    	if m.distance < 0.7*n.distance:
            gooods.append([m])
            good.append((m.trainIdx, m.queryIdx))
    
    if len(good)<4:
        continue
    matchedPointsCurrent = np.float32(
    				[kp1[i].pt for (__, i) in good]
    			)
    matchedPointsPrev = np.float32(
    				[kp2[i].pt for (i, __) in good]
    				)
    print(good)
    H, __ = cv.findHomography(matchedPointsCurrent, matchedPointsPrev, cv.RANSAC, 4)
    img3 = cv.drawMatchesKnn(leftImage,kp1,each,kp2,gooods,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    cv.imshow("lll",img3)
    cv.waitKey()

    txyz = np.dot(H, np.array([each.shape[1], each.shape[0], 1]))
    txyz = txyz/txyz[-1]
    dsize = (int(txyz[0])+leftImage.shape[1], int(txyz[1])+leftImage.shape[0])
    
    tmp = cv.warpPerspective(leftImage, H, dsize)
    
    tmp = mix_and_match(tmp,each)
    leftImage = tmp
    cv.imshow("lll",tmp)
    cv.waitKey()
# cv.imshow("lll", leftImage)
# cv.waitKey()

# cv.imshow("lll", a)
# cv.waitKey(0)