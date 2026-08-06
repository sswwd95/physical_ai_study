"""예제 12. BGR에서 Grayscale 변환

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

bgr_image = cv2.imread(image_path)

if bgr_image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

    print("컬러 이미지 shape:", bgr_image.shape)
    print("흑백 이미지 shape:", gray_image.shape)

    cv2.imshow("BGR Image", bgr_image)
    cv2.imshow("Gray Image", gray_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
