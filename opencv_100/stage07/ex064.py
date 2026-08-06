"""예제 64. 초록색 객체 검출

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

image_path = "practice_images/green_object.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_green = np.array([40, 80, 80])
    upper_green = np.array([80, 255, 255])

    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    green_result = cv2.bitwise_and(image, image, mask=green_mask)

    cv2.imshow("Original Image", image)
    cv2.imshow("Green Mask", green_mask)
    cv2.imshow("Green Object Result", green_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
