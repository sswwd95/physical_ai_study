"""예제 32. Gaussian Blur

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gaussian_3 = cv2.GaussianBlur(image, (3, 3), 0)
    gaussian_7 = cv2.GaussianBlur(image, (7, 7), 0)
    gaussian_15 = cv2.GaussianBlur(image, (15, 15), 0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur 3x3", gaussian_3)
    cv2.imshow("Gaussian Blur 7x7", gaussian_7)
    cv2.imshow("Gaussian Blur 15x15", gaussian_15)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
