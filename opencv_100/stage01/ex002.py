"""예제 2. 이미지 파일 읽기

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
    print("파일 경로를 확인하세요:", image_path)
else:
    print("이미지를 성공적으로 읽었습니다.")
    print("이미지 데이터 타입:", type(image))
