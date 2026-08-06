"""예제 28. 이미지 패딩

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    padded_image = cv2.copyMakeBorder(
        image,
        top=50,
        bottom=50,
        left=100,
        right=100,
        borderType=cv2.BORDER_CONSTANT,
        value=(0, 0, 0)
    )

    print("원본 크기:", image.shape)
    print("패딩 후 크기:", padded_image.shape)

    cv2.imshow("Original Image", image)
    cv2.imshow("Padded Image", padded_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
