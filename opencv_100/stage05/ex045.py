"""예제 45. Contour 면적 계산

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
            cv2.drawContours(
                result,
                [contour],
                -1,
                (0, 255, 0),
                2
            )
            print("검출된 객체 면적:", area)

    cv2.imshow("Binary Image", binary)
    cv2.imshow("Filtered Contours", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
