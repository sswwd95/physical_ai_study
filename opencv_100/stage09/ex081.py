"""예제 81. cv_bridge 개념

초보자용 상세 주석판입니다.

읽는 순서:
1. 위에서 아래로 주석을 먼저 읽습니다.
2. 바로 아래 코드가 어떤 작업을 하는지 확인합니다.
3. 실행 후 나타나는 창이나 터미널 결과를 비교합니다.

실행 위치: 이 프로젝트의 opencv_100 폴더
주의: cv2.imshow()가 있는 예제는 화면 창에서 아무 키나 눌러야 종료됩니다.
"""

# ROS2 Image 메시지와 OpenCV 이미지 배열을 서로 변환하는 CvBridge를 불러옵니다.
from cv_bridge import CvBridge

# ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 만듭니다.
bridge = CvBridge()

# 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환합니다.
cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

# OpenCV 이미지 배열을 ROS2 Image 메시지로 변환합니다.
ros_image_msg = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
