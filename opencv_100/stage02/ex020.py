"""예제 20. Otsu Threshold

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

    ret, otsu_binary = cv2.threshold(
        gray_image,
        0,
        255,
        cv2.THRESH_BINARY + cv2.THRESH_OTSU
    )

    print("Otsu가 자동으로 찾은 Threshold 값:", ret)

    cv2.imshow("Gray Image", gray_image)
    cv2.imshow("Otsu Threshold", otsu_binary)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
