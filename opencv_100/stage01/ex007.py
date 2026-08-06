# ============================================================================
# 노션 원문 학습 설명: 예제 7. BGR 색상 구조 이해
# ============================================================================
#
# [핵심 주제]
# OpenCV는 컬러 이미지를 RGB가 아니라 BGR 순서로 다룹니다.
#
# 일반적으로 사람은 색을 다음 순서로 생각함
#
# R: Red
# G: Green
# B: Blue
#
# 하지만 OpenCV는 기본적으로 다음 순서를 사용
#
# B: Blue
# G: Green
# R: Red
#
# [실습 목표]
# 1. OpenCV의 BGR 구조 이해
# 2. 빈 이미지 생성
# 3. 파란색, 초록색, 빨간색 이미지 만들기
# 4. 색상 채널 순서 확인
#
# [실무에서 자주 하는 실수]
# 실수 1. RGB 순서로 색을 넣음
#
# 초보자가 빨간색을 만들려고 다음처럼 작성하는 경우가 많습니다.
#
# image[:, :] = (255, 0, 0)
#
# 하지만 OpenCV에서는 이것이 빨간색이 아니라 파란색임
#
# 빨간색은 다음임
#
# image[:, :] = (0, 0, 255)
#
# 실수 2. matplotlib에서 색이 이상하게 나옴
#
# OpenCV 이미지를 matplotlib로 출력하면 색상이 이상하게 보일 수 있음
#
# 이유는 다음과 같습니다.
#
# OpenCV: BGR
# matplotlib: RGB
#
# 그래서 matplotlib로 출력하기 전에는 보통 변환이 필요
#
# rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
#
# [ROS2와 연결되는 포인트]
# ROS2 카메라 메시지에는 encoding 정보가 있음
#
# 예를 들어 다음과 같은 encoding이 있을 수 있음
#
# bgr8
# rgb8
# mono8
#
# OpenCV는 보통 `bgr8`과 잘 맞습니다.
#
# ROS2에서 이미지 색상이 이상하다면 encoding과 BGR/RGB 변환을 먼저 의심필요
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 모든 픽셀값이 0인 검은색 배열을 원하는 크기로 생성
blue_image = np.zeros((300, 300, 3), dtype=np.uint8)
green_image = np.zeros((300, 300, 3), dtype=np.uint8)
red_image = np.zeros((300, 300, 3), dtype=np.uint8)

blue_image[:, :] = (255, 0, 0)
green_image[:, :] = (0, 255, 0)
red_image[:, :] = (0, 0, 255)

# 처리 결과 확인용 OpenCV 창 표시
cv2.imshow("Blue Image", blue_image)
cv2.imshow("Green Image", green_image)
cv2.imshow("Red Image", red_image)

# 키 입력 대기 및 실시간 영상 갱신
cv2.waitKey(0)
# 모든 OpenCV 이미지 창 닫기
cv2.destroyAllWindows()
