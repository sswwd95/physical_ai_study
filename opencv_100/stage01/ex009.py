"""예제 9. 이미지 픽셀 값 수정

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    image[100, 150] = (0, 0, 255)

    image[120:170, 200:250] = (255, 0, 0)

    cv2.imshow("Modified Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
