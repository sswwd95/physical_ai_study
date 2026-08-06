"""예제 40. 실시간 카메라 블러 처리

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

        blurred_frame = cv2.GaussianBlur(frame, (7, 7), 0)

        cv2.imshow("Original Camera", frame)
        cv2.imshow("Blurred Camera", blurred_frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
