"""예제 31. 평균 블러

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    blur_3 = cv2.blur(image, (3, 3))
    blur_7 = cv2.blur(image, (7, 7))
    blur_15 = cv2.blur(image, (15, 15))

    cv2.imshow("Original Image", image)
    cv2.imshow("Average Blur 3x3", blur_3)
    cv2.imshow("Average Blur 7x7", blur_7)
    cv2.imshow("Average Blur 15x15", blur_15)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
