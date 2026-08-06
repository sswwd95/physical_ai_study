"""예제 25. 이미지 뒤집기

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    flip_horizontal = cv2.flip(image, 1)
    flip_vertical = cv2.flip(image, 0)
    flip_both = cv2.flip(image, -1)

    cv2.imshow("Original Image", image)
    cv2.imshow("Flip Horizontal", flip_horizontal)
    cv2.imshow("Flip Vertical", flip_vertical)
    cv2.imshow("Flip Both", flip_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
