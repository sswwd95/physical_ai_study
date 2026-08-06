# ============================================================================
# 노션 원문 학습 설명: 예제 35. Sharpening
# ============================================================================
#
# [핵심 주제]
# Sharpening은 이미지를 더 선명하게 만드는 필터임
#
# 흐릿한 이미지에서 경계와 세부 정보를 강조할 때 사용
#
# [실습 목표]
# 1. Sharpening 개념 이해
# 2. 커널 기반 필터 이해
# 3. cv2.filter2D() 사용법 이해
# 4. 이미지 선명화 결과 확인
#
# [실무에서 자주 하는 실수]
# 실수 1. 노이즈가 많은 이미지에 Sharpening을 바로 적용
#
# Sharpening은 경계뿐 아니라 노이즈도 함께 강조할 수 있음
#
# 따라서 노이즈가 많은 이미지에는 먼저 약한 블러를 적용하는 것이 좋습니다.
#
# 노이즈 많은 이미지
# → Gaussian Blur
# → Sharpening
#
# 실수 2. 선명화를 과도하게 적용
#
# 선명화를 너무 강하게 하면 이미지가 인위적으로 보이고, Edge나 Contour 검출에서 오히려 오류가 늘어날 수 있음
#
# [ROS2와 연결되는 포인트]
# Sharpening은 다음 상황에서 제한적으로 사용 가능
#
# 1. 카메라 초점이 약간 흐릴 때
# 2. 부품 경계를 더 뚜렷하게 보고 싶을 때
# 3. 검사 이미지에서 결함 경계를 강조할 때
#
# 하지만 실시간 주행 제어에서는 노이즈까지 커질 수 있으므로 조심해서 사용필요
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
    # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
    sharpening_kernel = np.array([
        [0, -1, 0],
        [-1, 5, -1],
        [0, -1, 0]
    ])

    # 직접 만든 커널을 이미지에 적용하여 필터링함
    sharpened_image = cv2.filter2D(image, -1, sharpening_kernel)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Sharpened Image", sharpened_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
