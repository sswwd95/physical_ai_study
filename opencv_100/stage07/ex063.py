# ============================================================================
# 노션 원문 학습 설명: 예제 63. 파란색 객체 검출
# ============================================================================
#
# [핵심 주제]
# HSV 색상 공간에서 파란색 객체를 검출
#
# 파란색은 빨간색보다 범위 설정이 비교적 단순함
#
# 일반적으로 OpenCV HSV 기준으로 다음 범위에서 시작할 수 있음
#
# H: 100 ~ 130
# S: 100 ~ 255
# V: 100 ~ 255
#
# [실습 목표]
# 1. 파란색 HSV 범위 설정
# 2. 파란색 마스크 생성
# 3. 파란색 영역 추출
# 4. 색상 객체 검출 흐름 반복 이해
#
# [준비 파일]
# 파란색 물체가 포함된 이미지를 준비함
#
# practice_images/blue_object.jpg
#
# [실무에서 자주 하는 실수]
# 실수 1. 파란색 계열 차이를 고려하지 않음
#
# 파란색도 여러 종류가 있음
#
# 하늘색
# 진한 파랑
# 남색
# 청록색에 가까운 파랑
#
# 각 색은 HSV Hue 범위가 다를 수 있음
#
# 실수 2. 조명 때문에 검출이 흔들림
#
# 밝기 값 V가 낮으면 같은 파란색도 검출되지 않을 수 있음
#
# 어두운 환경에서는 `lower_blue`의 V 값을 낮춰야 할 수 있음
#
# lower_blue = np.array([100, 80, 50])
#
# [ROS2와 연결되는 포인트]
# 파란색 마커 추적은 교육용 로봇에서 많이 사용
#
# 파란색 표식 검출
# → 중심 좌표 계산
# → 화면 중앙 기준 error_x 계산
# → 로봇 회전 제어
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/blue_object.jpg"

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
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
    blue_mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 마스크가 흰색인 위치만 원본 이미지에서 남깁니다.
    blue_result = cv2.bitwise_and(image, image, mask=blue_mask)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Blue Mask", blue_mask)
    cv2.imshow("Blue Object Result", blue_result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
