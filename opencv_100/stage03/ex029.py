"""예제 29. 이미지 피라미드 축소

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    down1 = cv2.pyrDown(image)
    down2 = cv2.pyrDown(down1)

    print("원본 크기:", image.shape)
    print("1단계 축소:", down1.shape)
    print("2단계 축소:", down2.shape)

    cv2.imshow("Original Image", image)
    cv2.imshow("Pyramid Down 1", down1)
    cv2.imshow("Pyramid Down 2", down2)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
