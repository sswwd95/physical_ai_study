# ============================================================================
# 노션 원문 학습 설명: 예제 81. cv_bridge 개념
# ============================================================================
#
# [핵심 주제]
# `cv_bridge`는 ROS2의 `sensor_msgs/Image` 메시지와 OpenCV 이미지 배열을 서로 변환해 주는 도구입니다.
#
# ROS2 카메라 Topic은 일반 Python NumPy 배열이 아니라 ROS2 메시지 형식임
#
# 따라서 OpenCV로 처리하려면 변환이 필요
#
# ROS2 Image 메시지
# → cv_bridge
# → OpenCV 이미지, 즉 NumPy 배열
#
# 반대로 OpenCV 처리 결과를 다시 ROS2 Topic으로 보내려면 다음 변환이 필요
#
# OpenCV 이미지
# → cv_bridge
# → ROS2 Image 메시지
#
# [실습 목표]
# 1. cv_bridge가 필요한 이유 이해
# 2. ROS2 Image와 OpenCV frame 차이 이해
# 3. imgmsg_to_cv2() 개념 이해
# 4. cv2_to_imgmsg() 개념 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. encoding을 확인하지 않음
#
# ROS2 카메라 메시지는 다음 encoding을 가질 수 있음
#
# bgr8
# rgb8
# mono8
#
# OpenCV는 기본적으로 BGR을 많이 사용
#
# 색상이 이상하게 보이면 encoding 문제를 먼저 확인필요
#
# 실수 2. ROS2 메시지를 OpenCV 함수에 바로 넣음
#
# 다음 코드는 잘못된 방식임
#
# cv2.imshow("camera", msg)
#
# `msg`는 OpenCV 이미지가 아니라 ROS2 메시지입니다.
#
# 반드시 변환필요
#
# frame = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
# cv2.imshow("camera", frame)
#
# [ROS2와 연결되는 포인트]
# ROS2 비전 노드의 기본 구조는 대부분 다음과 같습니다.
#
# Image Subscriber
# → cv_bridge 변환
# → OpenCV 처리
# → 결과 Publish
#
# 따라서 `cv_bridge`는 ROS2와 OpenCV를 연결하는 핵심 다리임
# ============================================================================
# ROS2 Image 메시지와 OpenCV 이미지 배열을 서로 변환하는 CvBridge를 불러오기
from cv_bridge import CvBridge

# ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 생성
bridge = CvBridge()

# 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환
cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

# OpenCV 이미지 배열을 ROS2 Image 메시지로 변환
ros_image_msg = bridge.cv2_to_imgmsg(cv_image, encoding="bgr8")
