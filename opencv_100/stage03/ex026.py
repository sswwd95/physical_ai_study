"""예제 26. Affine Transform

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

    src_points = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    dst_points = np.float32([
        [70, 80],
        [220, 50],
        [80, 230]
    ])

    affine_matrix = cv2.getAffineTransform(src_points, dst_points)

    affine_image = cv2.warpAffine(image, affine_matrix, (width, height))

    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transform", affine_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
