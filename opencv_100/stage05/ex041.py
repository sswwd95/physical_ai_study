"""예제 41. Sobel Edge

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    sobel_x_abs = cv2.convertScaleAbs(sobel_x)
    sobel_y_abs = cv2.convertScaleAbs(sobel_y)

    sobel_combined = cv2.addWeighted(
        sobel_x_abs,
        0.5,
        sobel_y_abs,
        0.5,
        0
    )

    cv2.imshow("Gray Image", gray)
    cv2.imshow("Sobel X", sobel_x_abs)
    cv2.imshow("Sobel Y", sobel_y_abs)
    cv2.imshow("Sobel Combined", sobel_combined)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
