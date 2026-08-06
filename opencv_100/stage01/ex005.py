"""예제 5. 이미지 크기, 채널, 데이터 타입 확인

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    print("이미지 shape:", image.shape)
    print("이미지 dtype:", image.dtype)
    print("이미지 size:", image.size)

    height, width, channels = image.shape

    print("높이:", height)
    print("너비:", width)
    print("채널 수:", channels)
