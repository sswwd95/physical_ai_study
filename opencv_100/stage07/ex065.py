"""예제 65. 마스크 노이즈 제거

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

image_path = "practice_images/blue_object.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = np.ones((5, 5), np.uint8)

    opened_mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    cleaned_mask = cv2.morphologyEx(
        opened_mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    result = cv2.bitwise_and(image, image, mask=cleaned_mask)

    cv2.imshow("Original Mask", mask)
    cv2.imshow("Opened Mask", opened_mask)
    cv2.imshow("Cleaned Mask", cleaned_mask)
    cv2.imshow("Cleaned Result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
