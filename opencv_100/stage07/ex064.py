# ============================================================================
# 노션 원문 학습 설명: 예제 64. 초록색 객체 검출
# ============================================================================
#
# [핵심 주제]
# HSV 색상 공간에서 초록색 객체를 검출
#
# 일반적인 초록색 HSV 범위는 다음에서 시작할 수 있음
#
# H: 40 ~ 80
# S: 80 ~ 255
# V: 80 ~ 255
#
# [실습 목표]
# 1. 초록색 HSV 범위 설정
# 2. 초록색 마스크 생성
# 3. 초록색 객체 추출
# 4. 색상별 범위 설정 감각 익히기
#
# [준비 파일]
# 초록색 물체가 포함된 이미지를 준비함
#
# practice_images/green_object.jpg
#
# [실무에서 자주 하는 실수]
# 실수 1. 초록색과 노란색 경계를 혼동함
#
# 연두색이나 노란빛이 강한 초록색은 Hue 값이 예상보다 낮을 수 있음
#
# 필요하면 범위를 넓힙니다.
#
# lower_green = np.array([35, 60, 60])
# upper_green = np.array([85, 255, 255])
#
# 실수 2. 배경에 같은 색이 있는 경우
#
# 초록색 객체를 찾으려는데 배경에도 초록색이 많으면 잘못 검출됨
#
# 이때는 색상만 보지 말고 다음 조건을 추가필요
#
# 면적
# 위치
# 모양
# ROI
# 움직임
#
# [ROS2와 연결되는 포인트]
# 초록색 라인 기반 주행은 라인트레이싱 교육에서 자주 사용됨
#
# 카메라 프레임
# → HSV 변환
# → 초록색 마스크
# → ROI 하단 영역만 사용
# → Contour 중심 계산
# → /cmd_vel 제어
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/green_object.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
image = cv2.imread(image_path)

# 이미지 또는 검출 결과 생성 여부 확인
if image is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # 색상 검출이 쉬운 HSV 색상 공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
    lower_green = np.array([40, 80, 80])
    upper_green = np.array([80, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
    green_mask = cv2.inRange(hsv, lower_green, upper_green)

    # 마스크가 흰색인 위치만 원본 이미지에서 남깁니다.
    green_result = cv2.bitwise_and(image, image, mask=green_mask)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Green Mask", green_mask)
    cv2.imshow("Green Object Result", green_result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
