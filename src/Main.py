import cv2
import numpy as np
import os
import components.HandTrack as htp
from utils.screenshot import screenshot
from utils.invert import invert

brushthickness = 5
eraserthickness = 100
xp, yp = 0, 0
imgCanvas = np.zeros((720, 1280, 3), np.uint8)
folderPath = "src/resources"
myList = os.listdir(folderPath)
overlaylist = []
for inPath in myList:
	image = cv2.imread(f'{folderPath}/{inPath}')
	overlaylist.append(image)
header = overlaylist[0]
drawColor = (255, 0, 255)
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)
detector = htp.handDetector(detectionCon=0.85)

while True:
	success, img = cap.read()
	if not success:
		break
	img = cv2.flip(img, 1)
	img = detector.findHands(img)
	lmlist = detector.findPosition(img, draw=False)
	if len(lmlist) != 0:
		x1, y1 = lmlist[8][1:]
		x2, y2 = lmlist[12][1:]
		fingers = detector.fingersUp()
		if fingers[1] and fingers[2]:
			xp, yp = 0, 0
			cv2.rectangle(img, (x1, y1 - 25), (x2, y2 + 25), drawColor, cv2.FILLED)
			if y1 < 125:
				if 250 < x1 < 450:
					header = overlaylist[0]
					drawColor = (255, 0, 255)
				elif 550 < x1 < 750:
					header = overlaylist[1]
					drawColor = (255, 0, 0)
				elif 800 < x1 < 950:
					header = overlaylist[2]
					drawColor = (0, 255, 0)
				elif 1050 < x1 < 1200:
					header = overlaylist[3]
					drawColor = (0, 0, 0)
		if fingers[1] and not fingers[2]:
			cv2.circle(img, (x1, y1), 25, drawColor, cv2.FILLED)
			if xp == 0 and yp == 0:
				xp, yp = x1, y1
			if drawColor == (0, 0, 0):
				cv2.line(img, (xp, yp), (x1, y1), drawColor, eraserthickness)
				cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, eraserthickness)
			else:
				cv2.line(img, (xp, yp), (x1, y1), drawColor, brushthickness)
				cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushthickness)
			xp, yp = x1, y1
	imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
	_, imgInv = cv2.threshold(imgGray, 50, 255, cv2.THRESH_BINARY_INV)
	imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
	img = cv2.bitwise_and(img, imgInv)
	img = cv2.bitwise_or(img, imgCanvas)
	img[0:125, 0:1280] = header

	cv2.imshow("Image", img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		cv2.imshow("Canvas", imgCanvas)
	if cv2.waitKey(1) & 0xFF == ord('s'):
		fileName = screenshot()
		print(fileName)

cv2.destroyAllWindows()