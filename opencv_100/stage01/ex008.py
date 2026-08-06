"""예제 8. 이미지 픽셀 값 읽기

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    y = 100
    x = 150

    pixel = image[y, x]

    print("좌표 x:", x)
    print("좌표 y:", y)
    print("픽셀 BGR 값:", pixel)

    blue = pixel[0]
    green = pixel[1]
    red = pixel[2]

    print("Blue:", blue)
    print("Green:", green)
    print("Red:", red)
