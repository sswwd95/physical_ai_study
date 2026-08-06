# ============================================================================
# 노션 원문 학습 설명: 예제 18. Threshold 이진화
# ============================================================================
#
# [핵심 주제]
# Threshold는 이미지를 흰색과 검은색으로 나누는 처리임
#
# 기준값보다 크면 흰색
# 기준값보다 작으면 검은색
#
# 이진화는 로봇 비전에서 매우 중요
#
# 라인 검출
# 객체 영역 분리
# 마스크 생성
# Contour 검출
#
# [실습 목표]
# 1. Threshold 개념 이해
# 2. cv2.threshold() 사용법 이해
# 3. Grayscale 이미지 이진화
# 4. 기준값 변화에 따른 결과 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. 컬러 이미지에 바로 Threshold 적용
#
# Threshold는 보통 Grayscale 이미지에 적용하는 것이 기본임
#
# gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# 실수 2. 기준값을 고정하고 모든 환경에서 사용
#
# 조명이 바뀌면 적절한 Threshold 값도 변경
#
# 실내에서는 127이 적절할 수 있지만, 야외에서는 전혀 맞지 않을 수 있음
#
# 이때는 Adaptive Threshold나 Otsu Threshold가 필요
#
# [ROS2와 연결되는 포인트]
# 라인 트레이싱에서 가장 기본적인 흐름은 다음과 같습니다.
#
# 카메라 프레임
# → Grayscale
# → Threshold
# → 라인 영역 검출
# → 중심 좌표 계산
# → 주행 제어
#
# Threshold 결과는 이후 Contour 검출의 입력으로 자주 사용됨
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

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
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # threshold value 변수에 이후 처리에 사용할 값을 저장
    threshold_value = 127

    # 기준값을 이용해 이미지를 흰색과 검은색의 이진 이미지로 분할
    ret, binary_image = cv2.threshold(
        gray_image,
        threshold_value,
        255,
        cv2.THRESH_BINARY
    )

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("사용된 Threshold 값:", ret)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Gray Image", gray_image)
    cv2.imshow("Binary Image", binary_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
