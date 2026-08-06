"""예제 47. 최소 외접 원

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

    ret, binary = cv2.threshold(
        blurred,
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
    min_area = 500

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > min_area:
            (x, y), radius = cv2.minEnclosingCircle(contour)

            center = (int(x), int(y))
            radius = int(radius)

            cv2.circle(
                result,
                center,
                radius,
                (0, 255, 255),
                2
            )

            cv2.circle(
                result,
                center,
                5,
                (0, 0, 255),
                -1
            )

            print("중심:", center, "반지름:", radius)

    cv2.imshow("Min Enclosing Circle", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
