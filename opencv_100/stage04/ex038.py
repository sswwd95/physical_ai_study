"""예제 38. Salt & Pepper 노이즈 제거

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
    noisy_image = image.copy()

    noise_ratio = 0.02
    height, width = image.shape[:2]
    noise_count = int(height * width * noise_ratio)

    for _ in range(noise_count):
        y = np.random.randint(0, height)
        x = np.random.randint(0, width)

        if np.random.rand() < 0.5:
            noisy_image[y, x] = (0, 0, 0)
        else:
            noisy_image[y, x] = (255, 255, 255)

    denoised_image = cv2.medianBlur(noisy_image, 5)

    cv2.imshow("Original Image", image)
    cv2.imshow("Salt and Pepper Noise", noisy_image)
    cv2.imshow("Denoised by Median Blur", denoised_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
