# ============================================================================
# 노션 원문 학습 설명: 예제 19. Adaptive Threshold
# ============================================================================
#
# [핵심 주제]
# Adaptive Threshold는 이미지 전체에 하나의 기준값을 적용하지 않고, 주변 영역을 기준으로 픽셀마다 다른 기준값을 적용
#
# 조명이 고르지 않은 환경에서 유용
#
# [실습 목표]
# 1. 일반 Threshold 한계 이해
# 2. Adaptive Threshold 사용법 이해
# 3. 조명 변화에 강한 이진화 적용
# 4. blockSize와 C 값 의미 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. blockSize를 짝수로 설정
#
# 다음 코드는 오류가 날 수 있음
#
# adaptive_binary = cv2.adaptiveThreshold(
# gray_image,
# 255,
# cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
# cv2.THRESH_BINARY,
# 10,
# 2
# )
#
# `blockSize`는 반드시 홀수여야 합니다.
#
# 실수 2. 노이즈가 많은 이미지에 바로 적용
#
# Adaptive Threshold는 주변 영역을 기준으로 계산하므로 노이즈에도 민감할 수 있음
#
# 실무에서는 보통 먼저 블러 처리를 함
#
# gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
#
# 그 후 Adaptive Threshold를 적용하면 결과가 더 안정적일 수 있음
#
# [ROS2와 연결되는 포인트]
# 로봇이 실내를 이동할 때 조명이 고르지 않은 경우가 많습니다.
#
# 창가 근처는 밝음
# 책상 아래는 어두움
# 복도는 조명이 일정하지 않음
#
# 이때 일반 Threshold보다 Adaptive Threshold가 라인 검출이나 바닥 패턴 검출에 더 유리할 수 있음
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

    # 주변 밝기를 기준으로 영역마다 다른 임계값을 적용
    adaptive_binary = cv2.adaptiveThreshold(
        gray_image,                       # 입력 이미지: 흑백(Grayscale) 이미지
        255,                              # 조건을 만족했을 때 지정할 픽셀값
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,   # 주변 픽셀에 가중치를 주어 임계값 계산
        cv2.THRESH_BINARY,                # 임계값보다 크면 255, 작으면 0
        11,                               # 임계값 계산에 사용할 주변 영역 크기: 11×11
        2                                 # 계산된 임계값에서 뺄 값
    )

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Gray Image", gray_image)
    cv2.imshow("Adaptive Threshold", adaptive_binary)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
