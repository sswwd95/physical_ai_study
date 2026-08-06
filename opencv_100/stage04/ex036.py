"""예제 36. 엣지 보존 필터

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    edge_preserved = cv2.edgePreservingFilter(
        image,
        flags=1,
        sigma_s=60,
        sigma_r=0.4
    )

    cv2.imshow("Original Image", image)
    cv2.imshow("Edge Preserving Filter", edge_preserved)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
