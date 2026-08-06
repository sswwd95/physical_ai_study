# ============================================================================
# 노션 원문 학습 설명: 예제 61. HSV 색상 마스크
# ============================================================================
#
# [핵심 주제]
# HSV 색상 공간에서 특정 색상 범위에 해당하는 픽셀만 흰색으로 만들고, 나머지는 검은색으로 만드는 마스크를 생성
#
# 색상 기반 객체 검출의 시작점임
#
# [실습 목표]
# 1. BGR 이미지를 HSV로 변환
# 2. 특정 HSV 범위 지정
# 3. cv2.inRange()로 마스크 생성
# 4. 원본 이미지에서 해당 색상만 추출
#
# [실무에서 자주 하는 실수]
# 실수 1. HSV 범위를 RGB 기준으로 생각함
#
# OpenCV의 HSV 범위는 다음과 같습니다.
#
# H: 0 ~ 179
# S: 0 ~ 255
# V: 0 ~ 255
#
# Hue를 0~360으로 생각하면 범위 설정이 틀어집니다.
#
# 실수 2. 조명 변화 고려 없이 범위를 고정함
#
# 같은 물체라도 조명이 바뀌면 HSV 값이 변화
#
# 실무에서는 다음 조건을 테스트필요
#
# 밝은 조명
# 어두운 조명
# 그림자
# 햇빛
# 카메라 자동 화이트밸런스
#
# [ROS2와 연결되는 포인트]
# ROS2 색상 객체 추적 노드는 보통 다음 구조를 가집니다.
#
# /camera/image_raw
# → cv_bridge
# → BGR frame
# → HSV 변환
# → inRange 마스크
# → Contour 검출
# → 중심 좌표 계산
# → /target_position 발행
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/sample.jpg"

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
    lower_color = np.array([100, 100, 100])
    upper_color = np.array([130, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
    mask = cv2.inRange(hsv, lower_color, upper_color)

    # 마스크가 흰색인 위치만 원본 이미지에서 남깁니다.
    result = cv2.bitwise_and(image, image, mask=mask)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("HSV Mask", mask)
    cv2.imshow("Color Extract Result", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
