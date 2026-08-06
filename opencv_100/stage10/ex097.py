"""예제 97. 컨베이어 객체 카운팅

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

cap = cv2.VideoCapture(0)

count = 0
counted_centers = []

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        height, width = frame.shape[:2]

        line_y = height // 2

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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

        cv2.line(
            frame,
            (0, line_y),
            (width, line_y),
            (255, 0, 0),
            2
        )

        current_centers = []

        for contour in contours:
            area = cv2.contourArea(contour)

            if area > 500:
                x, y, w, h = cv2.boundingRect(contour)

                center_x = x + w // 2
                center_y = y + h // 2

                current_centers.append((center_x, center_y))

                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                cv2.circle(
                    frame,
                    (center_x, center_y),
                    5,
                    (0, 0, 255),
                    -1
                )

                if abs(center_y - line_y) < 10:
                    already_counted = False

                    for old_center in counted_centers:
                        old_x, old_y = old_center

                        distance = ((center_x - old_x) ** 2 + (center_y - old_y) ** 2) ** 0.5

                        if distance < 50:
                            already_counted = True
                            break

                    if not already_counted:
                        count += 1
                        counted_centers.append((center_x, center_y))
                        print("객체 카운트:", count)

        cv2.putText(
            frame,
            f"Count: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 255, 255),
            2
        )

        cv2.imshow("Conveyor Counting", frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
