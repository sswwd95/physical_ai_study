"""예제 98. 로봇 팔 Pick 위치 계산

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

image_path = "practice_images/workpiece.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    height, width = image.shape[:2]

    workspace_width_mm = 400
    workspace_height_mm = 300

    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    lower_object = np.array([20, 80, 80])
    upper_object = np.array([40, 255, 255])

    mask = cv2.inRange(hsv, lower_object, upper_object)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    result = image.copy()

    if len(contours) > 0:
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(largest_contour)

            center_x = x + w // 2
            center_y = y + h // 2

            robot_x_mm = center_x / width * workspace_width_mm
            robot_y_mm = center_y / height * workspace_height_mm

            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
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
                f"Pick mm: ({robot_x_mm:.1f}, {robot_y_mm:.1f})",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            print("픽셀 좌표:", center_x, center_y)
            print("로봇 Pick 좌표 근사 mm:", robot_x_mm, robot_y_mm)

    cv2.imshow("Pick Position", result)
    cv2.imshow("Mask", mask)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
