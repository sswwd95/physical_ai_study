# ============================================================================
# 노션 원문 학습 설명: 예제 11. BGR에서 RGB로 변환
# ============================================================================
#
# [핵심 주제]
# OpenCV는 이미지를 기본적으로 BGR 순서로 읽기
#
# OpenCV 기본 색상 순서 = B, G, R
# 일반적인 이미지 표시 순서 = R, G, B
#
# 그래서 OpenCV 이미지를 `matplotlib`, 딥러닝 모델, 일부 ROS2 이미지 처리 라이브러리와 함께 사용할 때는 RGB 변환이 필요할 수 있음
#
# [실습 목표]
# 1. OpenCV의 BGR 구조 복습
# 2. cv2.cvtColor() 사용법 이해
# 3. BGR 이미지를 RGB 이미지로 변환
# 4. 색상 순서가 바뀌면 결과가 달라지는 이유 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. matplotlib에 BGR 이미지를 그대로 넣음
#
# 다음 코드는 색상이 이상하게 보일 수 있음
#
# import matplotlib.pyplot as plt
#
# plt.imshow(bgr_image)
# plt.show()
#
# matplotlib은 RGB 순서로 이미지를 해석하기 때문임
#
# 올바른 방식은 다음과 같습니다.
#
# rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)
#
# plt.imshow(rgb_image)
# plt.show()
#
# 실수 2. 딥러닝 모델 입력 색상 순서를 확인하지 않음
#
# YOLO, PyTorch 모델, TensorFlow 모델을 사용할 때는 입력 이미지가 BGR인지 RGB인지 반드시 확인필요
#
# OpenCV 카메라 프레임: 보통 BGR
# 딥러닝 모델 입력: 보통 RGB인 경우가 많음
#
# 색상 순서가 맞지 않으면 객체 인식 정확도가 떨어질 수 있음
#
# [ROS2와 연결되는 포인트]
# ROS2 Image 메시지에는 `encoding` 정보가 있음
#
# 대표적으로 다음이 있음
#
# bgr8
# rgb8
# mono8
#
# OpenCV와 자연스럽게 연결하려면 보통 `bgr8`을 많이 사용
#
# cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")
#
# 하지만 딥러닝 모델로 넣기 전에는 RGB 변환이 필요할 수 있음
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/sample.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
bgr_image = cv2.imread(image_path)

# 이미지 또는 검출 결과 생성 여부 확인
if bgr_image is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # OpenCV의 BGR 채널 순서를 일반적인 RGB 순서로 바꿉니다.
    rgb_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2RGB)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("BGR Image - OpenCV Default", bgr_image)
    cv2.imshow("RGB Image - Converted", rgb_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
