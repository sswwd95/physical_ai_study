# ============================================================================
# 노션 원문 학습 설명: 예제 14. 특정 색상 영역 검출
# ============================================================================
#
# [핵심 주제]
# HSV 색상 공간에서 특정 색상 범위를 지정하고, 해당 색상 영역만 검출
#
# 이 예제에서는 파란색 영역 검출을 기준으로 설명함
#
# [실습 목표]
# 1. HSV 색상 범위 지정
# 2. cv2.inRange() 사용법 이해
# 3. 마스크 이미지 생성
# 4. 특정 색상 영역만 추출
#
# [실무에서 자주 하는 실수]
# 실수 1. 색상 범위를 고정값으로만 믿음
#
# 조명 환경에 따라 같은 파란색도 HSV 값이 변화 가능
#
# 밝은 조명
# 어두운 조명
# 그림자
# 카메라 자동 화이트밸런스
#
# 이런 조건에 따라 범위를 조정필요
#
# 실수 2. BGR에서 직접 색상 범위를 잡음
#
# BGR에서도 색상 범위 검출은 가능하지만 조명 변화에 약함
#
# 실무에서는 보통 HSV로 변환한 뒤 색상 범위를 잡습니다.
#
# [ROS2와 연결되는 포인트]
# 색상 기반 객체 검출은 ROS2 입문 로봇 프로젝트에서 매우 자주 사용됨
#
# 예를 들어 파란 공을 따라가는 로봇은 다음 구조를 가질 수 있음
#
# /camera/image_raw
# → OpenCV HSV 변환
# → 파란색 마스크 생성
# → Contour 검출
# → 중심 좌표 계산
# → /target_position Publish
# → 주행 제어 노드에서 /cmd_vel Publish
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

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
    # 색상 검출이 쉬운 HSV 색상 공간으로 변환
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
    mask = cv2.inRange(hsv_image, lower_blue, upper_blue)

    # 마스크가 흰색인 위치만 원본 이미지에서 남깁니다.
    blue_result = cv2.bitwise_and(bgr_image, bgr_image, mask=mask)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", bgr_image)
    cv2.imshow("Blue Mask", mask)
    cv2.imshow("Blue Area Result", blue_result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
