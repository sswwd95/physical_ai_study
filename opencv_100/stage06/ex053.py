"""예제 53. 키보드 입력으로 종료

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

        cv2.imshow("Keyboard Control Camera", frame)

        key = cv2.waitKey(1)

        if key == ord('q'):
            print("q 키 입력: 프로그램 종료")
            break

        elif key == ord('s'):
            print("s 키 입력: 현재 프레임 표시 중")

    cap.release()
    cv2.destroyAllWindows()
