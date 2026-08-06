"""예제 16. 이미지 대비 조절

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    low_contrast = cv2.convertScaleAbs(image, alpha=0.5, beta=0)
    high_contrast = cv2.convertScaleAbs(image, alpha=1.8, beta=0)

    cv2.imshow("Original Image", image)
    cv2.imshow("Low Contrast", low_contrast)
    cv2.imshow("High Contrast", high_contrast)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
