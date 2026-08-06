"""예제 7. BGR 색상 구조 이해

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

blue_image = np.zeros((300, 300, 3), dtype=np.uint8)
green_image = np.zeros((300, 300, 3), dtype=np.uint8)
red_image = np.zeros((300, 300, 3), dtype=np.uint8)

blue_image[:, :] = (255, 0, 0)
green_image[:, :] = (0, 255, 0)
red_image[:, :] = (0, 0, 255)

cv2.imshow("Blue Image", blue_image)
cv2.imshow("Green Image", green_image)
cv2.imshow("Red Image", red_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
