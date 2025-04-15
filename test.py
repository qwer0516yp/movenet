import cv2 as cv
img = cv.imread("E:\Photos\Owen_Personal\Ironman_hulkbuster.JPG")

cv.imshow("Display window", img)
k = cv.waitKey(0) # Wait for a keystroke in the window
