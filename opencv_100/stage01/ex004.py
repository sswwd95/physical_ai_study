"""예제 4. 이미지 저장

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"
save_path = "practice_images/output_sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    result = cv2.imwrite(save_path, image)

    if result:
        print("이미지 저장 성공:", save_path)
    else:
        print("이미지 저장 실패")
