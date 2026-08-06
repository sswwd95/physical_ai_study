"""예제 35. Sharpening

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
    sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpened Image", sharpened_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
