# ============================================================================
# 노션 원문 학습 설명: 예제 65. 마스크 노이즈 제거
# ============================================================================
#
# [핵심 주제]
# 색상 마스크에는 작은 점 노이즈가 생길 수 있음
#
# 이런 노이즈를 제거하지 않으면 Contour가 너무 많이 검출되고 객체 추적이 흔들립니다.
#
# 이번 예제에서는 Morphology 연산을 사용해 마스크를 정리함
#
# 대표 연산은 다음과 같습니다.
#
# Opening: 작은 흰 점 제거
# Closing: 객체 내부의 작은 구멍 메우기
#
# [실습 목표]
# 1. 색상 마스크의 노이즈 문제 이해
# 2. cv2.morphologyEx() 사용법 이해
# 3. Opening으로 작은 점 제거
# 4. Closing으로 구멍 메우기
#
# [실무에서 자주 하는 실수]
# 실수 1. 커널 크기를 너무 크게 설정
#
# 커널이 너무 크면 작은 객체까지 사라질 수 있음
#
# kernel = np.ones((15, 15), np.uint8)
#
# 처음에는 3×3 또는 5×5로 시작하는 것이 좋습니다.
#
# 실수 2. Opening과 Closing 순서를 이해하지 못함
#
# 일반적인 색상 마스크 정리 흐름은 다음과 같습니다.
#
# 마스크 생성
# → Opening으로 작은 흰 점 제거
# → Closing으로 객체 내부 구멍 메우기
#
# 하지만 이미지 상태에 따라 순서를 바꿔야 할 수도 있음
#
# [ROS2와 연결되는 포인트]
# ROS2 객체 추적에서 마스크 노이즈 제거는 매우 중요
#
# 마스크 노이즈 많음
# → Contour가 많이 생김
# → 중심 좌표가 흔들림
# → 로봇 제어가 흔들림
#
# 마스크를 정리하면 객체 중심이 안정되어 로봇 제어도 안정됨
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
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # 형태학적 연산이나 필터에 사용할 값이 1인 커널 배열을 생성
    kernel = np.ones((5, 5), np.uint8)

    # 작은 흰색 노이즈를 제거하기 위해 열기 연산을 적용
    opened_mask = cv2.morphologyEx(
        mask,
        cv2.MORPH_OPEN,
        kernel
    )

    # 객체 내부의 작은 검은 구멍을 메우기 위해 닫기 연산을 적용
    cleaned_mask = cv2.morphologyEx(
        opened_mask,
        cv2.MORPH_CLOSE,
        kernel
    )

    # 마스크가 흰색인 위치만 원본 이미지에서 남깁니다.
    result = cv2.bitwise_and(image, image, mask=cleaned_mask)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Mask", mask)
    cv2.imshow("Opened Mask", opened_mask)
    cv2.imshow("Cleaned Mask", cleaned_mask)
    cv2.imshow("Cleaned Result", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
