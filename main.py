import cv2
import numpy

cv2.namedWindow("output", cv2.WINDOW_NORMAL)

img = cv2.imread('Monocyte_40x.JPG', 0)

circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, dp=1, minDist=50, param1=180, param2=22, minRadius=10, maxRadius=60)

if circles is not None:
    circles = numpy.round(circles[0, :]).astype("int")

    index = 0
    for (x, y, r) in circles:
        cv2.circle(img, (x, y), r, (255, 255, 0), 2)
        cv2.rectangle(img, (x - 1, y - 1), (x + 1, y + 1), (255, 255, 0), 3)
        index = index + 1

    print('No. of circles detected = {}'.format(index))

    # outSized = cv2.resize(output, (950, 950))
    outSized = cv2.resize(img, (950, 950))
    # imgSized = cv2.resize(img, (950, 950))

    cv2.imshow("output", outSized)
    # cv2.imshow("output", numpy.hstack([imgSized, outSized]))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print('Can\'t find any circles!')
