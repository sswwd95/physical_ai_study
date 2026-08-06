# ============================================================================
# 노션 원문 학습 설명: 예제 62. 빨간색 객체 검출
# ============================================================================
#
# [핵심 주제]
# HSV에서 빨간색 객체를 검출
#
# 빨간색은 HSV Hue 값에서 특이한 점이 있음
#
# OpenCV Hue 범위가 0~179이기 때문에 빨간색은 양 끝에 걸쳐 있음
#
# 빨간색 범위 1: H 0 ~ 10
# 빨간색 범위 2: H 170 ~ 179
#
# 그래서 빨간색은 마스크를 두 개 만든 뒤 합치는 방식이 일반적임
#
# [실습 목표]
# 1. 빨간색 HSV 범위 이해
# 2. 빨간색 마스크 2개 생성
# 3. 두 마스크 합치기
# 4. 빨간색 객체만 추출
#
# [준비 파일]
# 빨간색 물체가 포함된 이미지를 준비함
#
# practice_images/red_object.jpg
#
# 예를 들어 빨간 공, 빨간 컵, 빨간 표식이 있는 이미지가 좋습니다.
#
# [실무에서 자주 하는 실수]
# 실수 1. 빨간색 범위를 하나만 사용함
#
# 다음처럼 하나만 쓰면 일부 빨간색이 검출되지 않을 수 있음
#
# lower_red = np.array([0, 100, 100])
# upper_red = np.array([10, 255, 255])
#
# 빨간색은 Hue 양 끝에 걸치므로 보통 두 범위를 사용
#
# 실수 2. S, V 최소값을 너무 낮게 설정
#
# S와 V 최소값이 너무 낮으면 회색, 어두운 그림자, 노이즈까지 빨간색으로 잡힐 수 있음
#
# S: 채도
# V: 밝기
#
# 초기값은 보통 100 정도에서 시작한 뒤 조정함
#
# [ROS2와 연결되는 포인트]
# 빨간 공 추적 로봇은 다음 흐름으로 만들 수 있음
#
# 카메라 프레임
# → HSV 변환
# → 빨간색 마스크
# → Contour 검출
# → 가장 큰 Contour 선택
# → 중심점 계산
# → 화면 중앙과 비교
# → /cmd_vel 제어
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/red_object.jpg"

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
    lower_red1 = np.array([0, 100, 100])
    upper_red1 = np.array([10, 255, 255])

    # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
    lower_red2 = np.array([170, 100, 100])
    upper_red2 = np.array([179, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
    mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
    mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

    # red mask 변수에 이후 처리에 사용할 값을 저장
    red_mask = cv2.bitwise_or(mask1, mask2)

    # 마스크가 흰색인 위치만 원본 이미지에서 남깁니다.
    red_result = cv2.bitwise_and(image, image, mask=red_mask)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Red Mask", red_mask)
    cv2.imshow("Red Object Result", red_result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
