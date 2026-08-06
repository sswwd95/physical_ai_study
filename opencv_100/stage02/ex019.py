"""예제 19. Adaptive Threshold

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    adaptive_binary = cv2.adaptiveThreshold(
        gray_image,
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )

    cv2.imshow("Gray Image", gray_image)
    cv2.imshow("Adaptive Threshold", adaptive_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
