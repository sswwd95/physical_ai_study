"""예제 81. cv_bridge 개념

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

from cv_bridge import CvBridge

bridge = CvBridge()

cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

ros_image_msg = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
