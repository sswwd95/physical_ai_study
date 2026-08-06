"""예제 92. 차선 중심 계산

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        height, width = frame.shape[:2]
        image_center_x = width // 2

        roi_start_y = int(height * 0.6)
        roi = frame[roi_start_y:height, 0:width]

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        ret, binary = cv2.threshold(
            blurred,
            100,
            255,
            cv2.THRESH_BINARY_INV
        )

        contours, _ = cv2.findContours(
            binary,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        cv2.line(
            frame,
            (image_center_x, 0),
            (image_center_x, height),
            (255, 0, 0),
            2
        )

        if len(contours) > 0:
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)

            if area > 300:
                moments = cv2.moments(largest_contour)

                if moments["m00"] != 0:
                    line_center_x = int(moments["m10"] / moments["m00"])
                    line_center_y = int(moments["m01"] / moments["m00"])

                    line_center_y_on_frame = line_center_y + roi_start_y

                    error_x = line_center_x - image_center_x

                    cv2.drawContours(
                        roi,
                        [largest_contour],
                        -1,
                        (0, 255, 0),
                        2
                    )

                    cv2.circle(
                        frame,
                        (line_center_x, line_center_y_on_frame),
                        8,
                        (0, 0, 255),
                        -1
                    )

                    cv2.putText(
                        frame,
                        f"error_x: {error_x}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 255),
                        2
                    )

                    print("라인 중심:", line_center_x, line_center_y_on_frame)
                    print("화면 중앙 대비 오차:", error_x)

        cv2.imshow("Line Center Frame", frame)
        cv2.imshow("Line Binary", binary)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
