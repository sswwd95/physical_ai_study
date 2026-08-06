"""예제 75. ORB 특징점 검출

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=500)

    keypoints, descriptors = orb.detectAndCompute(gray, None)

    result = cv2.drawKeypoints(
        image,
        keypoints,
        None,
        color=(0, 255, 0),
        flags=0
    )

    print("검출된 특징점 개수:", len(keypoints))

    if descriptors is not None:
        print("Descriptor shape:", descriptors.shape)

    cv2.imshow("ORB Keypoints", result)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
