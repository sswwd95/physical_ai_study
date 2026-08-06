"""예제 33. Median Blur

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    median_3 = cv2.medianBlur(image, 3)
    median_5 = cv2.medianBlur(image, 5)
    median_9 = cv2.medianBlur(image, 9)

    cv2.imshow("Original Image", image)
    cv2.imshow("Median Blur 3", median_3)
    cv2.imshow("Median Blur 5", median_5)
    cv2.imshow("Median Blur 9", median_9)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
