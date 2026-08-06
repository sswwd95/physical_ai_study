"""예제 37. 노이즈 이미지 생성

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
    noise = np.random.normal(
        loc=0,
        scale=25,
        size=image.shape
    ).astype(np.int16)

    noisy_image = image.astype(np.int16) + noise
    noisy_image = np.clip(noisy_image, 0, 255)
    noisy_image = noisy_image.astype(np.uint8)

    cv2.imshow("Original Image", image)
    cv2.imshow("Noisy Image", noisy_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
