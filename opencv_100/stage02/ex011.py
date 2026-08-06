"""예제 11. BGR에서 RGB로 변환

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

bgr_image = cv2.imread(image_path)

if bgr_image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    cv2.imshow("BGR Image - OpenCV Default", bgr_image)
    cv2.imshow("RGB Image - Converted", rgb_image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
