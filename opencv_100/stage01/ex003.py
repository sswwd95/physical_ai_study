"""예제 3. 이미지 화면 출력

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image_path = "practice_images/sample.jpg"

image = cv2.imread(image_path)

if image is None:
    print("이미지를 읽을 수 없습니다.")
else:
    cv2.imshow("Sample Image", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
