"""예제 44. Contour 검출

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

    ret, binary = cv2.threshold(
        gray,
        127,
        255,
        cv2.THRESH_BINARY
    )

    contours, hierarchy = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = image.copy()

    cv2.drawContours(
        result,
        contours,
        -1,
        (0, 0, 255),
        2
    )

    print("검출된 Contour 개수:", len(contours))

    cv2.imshow("Binary Image", binary)
    cv2.imshow("Contour Result", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
