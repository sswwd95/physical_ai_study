"""예제 49. 도형 분류

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/shapes.png"

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
    min_area = 300

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > min_area:
            perimeter = cv2.arcLength(contour, True)

            approx = cv2.approxPolyDP(
                contour,
                0.02 * perimeter,
                True
            )

            vertices = len(approx)

            if vertices == 3:
                shape_name = "Triangle"
            elif vertices == 4:
                shape_name = "Rectangle"
            else:
                shape_name = "Circle or Other"

            x, y, w, h = cv2.boundingRect(approx)

            cv2.drawContours(
                result,
                [approx],
                -1,
                (0, 255, 0),
                2
            )

            cv2.putText(
                result,
                shape_name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

    cv2.imshow("Binary Image", binary)
    cv2.imshow("Shape Classification", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
