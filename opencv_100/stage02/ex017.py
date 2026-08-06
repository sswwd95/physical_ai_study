"""예제 17. 이미지 반전

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    inverted_color = cv2.bitwise_not(image)
    inverted_gray = cv2.bitwise_not(gray_image)

    cv2.imshow("Original Color", image)
    cv2.imshow("Inverted Color", inverted_color)
    cv2.imshow("Original Gray", gray_image)
    cv2.imshow("Inverted Gray", inverted_gray)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
