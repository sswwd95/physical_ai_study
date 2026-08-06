"""예제 7. BGR 색상 구조 이해

초보자용 상세 주석판입니다.

읽는 순서:
1. 위에서 아래로 주석을 먼저 읽습니다.
2. 바로 아래 코드가 어떤 작업을 하는지 확인합니다.
3. 실행 후 나타나는 창이나 터미널 결과를 비교합니다.

실행 위치: 이 프로젝트의 opencv_100 폴더
주의: cv2.imshow()가 있는 예제는 화면 창에서 아무 키나 눌러야 종료됩니다.
"""

# OpenCV 기능을 사용하기 위해 cv2 모듈을 불러옵니다.
import cv2
# 이미지 배열과 수치 계산을 위해 NumPy를 np라는 이름으로 불러옵니다.
import numpy as np

# 모든 픽셀값이 0인 검은색 배열을 원하는 크기로 만듭니다.
blue_image = np.zeros((300, 300, 3), dtype=np.uint8)
green_image = np.zeros((300, 300, 3), dtype=np.uint8)
red_image = np.zeros((300, 300, 3), dtype=np.uint8)

blue_image[:, :] = (255, 0, 0)
green_image[:, :] = (0, 255, 0)
red_image[:, :] = (0, 0, 255)

# 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
cv2.imshow("Blue Image", blue_image)
cv2.imshow("Green Image", green_image)
cv2.imshow("Red Image", red_image)

# 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
cv2.waitKey(0)
# OpenCV가 만든 모든 이미지 창을 닫습니다.
cv2.destroyAllWindows()
