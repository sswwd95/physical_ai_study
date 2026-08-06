"""예제 22. 비율 유지 Resize

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    original_height, original_width = image.shape[:2]

    target_width = 320
    ratio = target_width / original_width
    target_height = int(original_height * ratio)

    resized_image = cv2.resize(image, (target_width, target_height))

    print("원본 크기:", image.shape)
    print("비율 유지 Resize 크기:", resized_image.shape)

    cv2.imshow("Original Image", image)
    cv2.imshow("Aspect Ratio Resized Image", resized_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
