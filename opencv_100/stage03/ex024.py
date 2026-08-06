"""예제 24. 이미지 이동

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
    height, width = image.shape[:2]

    move_x = 100
    move_y = 50

    translation_matrix = np.float32([
        [1, 0, move_x],
        [0, 1, move_y]
    ])

    moved_image = cv2.warpAffine(image, translation_matrix, (width, height))

    cv2.imshow("Original Image", image)
    cv2.imshow("Moved Image", moved_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
