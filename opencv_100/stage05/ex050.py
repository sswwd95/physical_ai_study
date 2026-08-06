"""예제 50. 객체 중심점 계산

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

    height, width = image.shape[:2]
    image_center_x = width // 2

    cv2.line(
        result,
        (image_center_x, 0),
        (image_center_x, height),
        (255, 0, 0),
        2
    )

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > min_area:
            moments = cv2.moments(contour)

            if moments["m00"] != 0:
                center_x = int(moments["m10"] / moments["m00"])
                center_y = int(moments["m01"] / moments["m00"])

                error_x = center_x - image_center_x

                cv2.drawContours(
                    result,
                    [contour],
                    -1,
                    (0, 255, 0),
                    2
                )

                cv2.circle(
                    result,
                    (center_x, center_y),
                    6,
                    (0, 0, 255),
                    -1
                )

                cv2.putText(
                    result,
                    f"Center: ({center_x}, {center_y})",
                    (center_x + 10, center_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    2
                )

                cv2.putText(
                    result,
                    f"Error X: {error_x}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )

                print("객체 중심:", center_x, center_y)
                print("화면 중앙 대비 x 오차:", error_x)

    cv2.imshow("Binary Image", binary)
    cv2.imshow("Object Center", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
