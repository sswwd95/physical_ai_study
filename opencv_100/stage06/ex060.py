"""예제 60. 카메라 프레임 캡처

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import os

save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라를 열 수 없습니다.")
else:
    count = 0

    while True:
        ret, frame = cap.read()

        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("Capture Camera", frame)

        key = cv2.waitKey(1)

        if key == ord('s'):
            file_path = os.path.join(save_dir, f"capture_{count:04d}.jpg")
            cv2.imwrite(file_path, frame)
            print("이미지 저장:", file_path)
            count += 1

        elif key == ord('q'):
            print("프로그램 종료")
            break

    cap.release()
    cv2.destroyAllWindows()
