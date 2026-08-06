"""예제 39. 이미지 스무딩 비교

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    average_blur = cv2.blur(image, (7, 7))
    gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)
    median_blur = cv2.medianBlur(image, 7)
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    cv2.imshow("Original Image", image)
    cv2.imshow("Average Blur", average_blur)
    cv2.imshow("Gaussian Blur", gaussian_blur)
    cv2.imshow("Median Blur", median_blur)
    cv2.imshow("Bilateral Filter", bilateral)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
