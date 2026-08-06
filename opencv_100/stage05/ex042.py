"""예제 42. Laplacian Edge

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
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    laplacian_abs = cv2.convertScaleAbs(laplacian)

    cv2.imshow("Gray Image", gray)
    cv2.imshow("Blurred Image", blurred)
    cv2.imshow("Laplacian Edge", laplacian_abs)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
