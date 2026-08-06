"""예제 61. HSV 색상 마스크

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_color = np.array([100, 100, 100])
    upper_color = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_color, upper_color)

    result = cv2.bitwise_and(image, image, mask=mask)

    cv2.imshow("Original Image", image)
    cv2.imshow("HSV Mask", mask)
    cv2.imshow("Color Extract Result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
