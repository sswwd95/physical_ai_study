"""예제 94. QR 코드 검출

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

cap = cv2.VideoCapture(0)

qr_detector = cv2.QRCodeDetector()

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        data, points, straight_qrcode = qr_detector.detectAndDecode(frame)

        if points is not None:
            points = points.astype(int)

            for i in range(len(points[0])):
                pt1 = tuple(points[0][i])
                pt2 = tuple(points[0][(i + 1) % len(points[0])])

                cv2.line(
                    frame,
                    pt1,
                    pt2,
                    (0, 255, 0),
                    2
                )

            if data:
                cv2.putText(
                    frame,
                    data,
                    tuple(points[0][0]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

                print("QR 데이터:", data)

        cv2.imshow("QR Code Detection", frame)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
