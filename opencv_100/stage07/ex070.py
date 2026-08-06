"""예제 70. ROS2 Topic 변환 준비

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

def detect_blue_objects(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    kernel = np.ones((5, 5), np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    contours, hierarchy = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    objects = []

    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 500:
            x, y, w, h = cv2.boundingRect(contour)

            center_x = x + w // 2
            center_y = y + h // 2

            obj = {
                "center_x": center_x,
                "center_y": center_y,
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "area": area
            }

            objects.append(obj)

    return objects, mask

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        objects, mask = detect_blue_objects(frame)

        for index, obj in enumerate(objects):
            x = obj["x"]
            y = obj["y"]
            w = obj["width"]
            h = obj["height"]
            center_x = obj["center_x"]
            center_y = obj["center_y"]
            area = obj["area"]

            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            cv2.putText(
                frame,
                f"Obj {index} Area {int(area)}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2
            )

        print("ROS2 Topic으로 보낼 객체 목록:", objects)

        cv2.imshow("ROS2 Ready Detection", frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
