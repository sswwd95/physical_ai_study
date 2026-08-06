"""예제 56. 비디오 파일 읽기

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

video_path = "practice_videos/sample.mp4"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("비디오 파일을 열 수 없습니다.")
else:
    while True:
        ret, frame = cap.read()

        if not ret:
            print("비디오가 끝났거나 프레임을 읽을 수 없습니다.")
            break

        cv2.imshow("Video File", frame)

        if cv2.waitKey(30) == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
