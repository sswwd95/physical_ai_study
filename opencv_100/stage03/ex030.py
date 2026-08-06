"""예제 30. 이미지 피라미드 확대

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    down_image = cv2.pyrDown(image)
    up_image = cv2.pyrUp(down_image)

    print("원본 크기:", image.shape)
    print("축소 이미지 크기:", down_image.shape)
    print("다시 확대한 이미지 크기:", up_image.shape)

    cv2.imshow("Original Image", image)
    cv2.imshow("Pyramid Down", down_image)
    cv2.imshow("Pyramid Up After Down", up_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
