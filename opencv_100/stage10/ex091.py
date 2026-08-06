"""예제 91. 라인 트레이싱 전처리

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

        roi = frame[int(height * 0.6):height, 0:width]

        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)

        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        ret, binary = cv2.threshold(
            blurred,
            100,
            255,
            cv2.THRESH_BINARY_INV
        )

        cv2.imshow("Original Frame", frame)
        cv2.imshow("Line ROI", roi)
        cv2.imshow("Line Binary", binary)

        if cv2.waitKey(1) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
