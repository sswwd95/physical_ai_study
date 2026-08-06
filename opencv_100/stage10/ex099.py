"""예제 99. OpenCV + YOLO 연계 준비

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2
import numpy as np

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    input_size = 640

    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    resized = cv2.resize(rgb_image, (input_size, input_size))

    normalized = resized.astype(np.float32) / 255.0

    chw = np.transpose(normalized, (2, 0, 1))

    batch = np.expand_dims(chw, axis=0)

    print("원본 shape:", image.shape)
    print("RGB Resize shape:", resized.shape)
    print("정규화 범위:", normalized.min(), normalized.max())
    print("CHW shape:", chw.shape)
    print("Batch shape:", batch.shape)

    cv2.imshow("Original BGR", image)
    cv2.imshow("YOLO Input Preview", cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))

    cv2.waitKey(0)
    cv2.destroyAllWindows()
