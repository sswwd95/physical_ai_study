"""예제 14. 특정 색상 영역 검출

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

image_path = "practice_images/sample.jpg"

bgr_image = cv2.imread(image_path)

if bgr_image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    blue_result = cv2.bitwise_and(bgr_image, bgr_image, mask=mask)

    cv2.imshow("Original Image", bgr_image)
    cv2.imshow("Blue Mask", mask)
    cv2.imshow("Blue Area Result", blue_result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
