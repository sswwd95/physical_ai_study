# ============================================================================
# 노션 원문 학습 설명: 예제 32. Gaussian Blur
# ============================================================================
#
# [핵심 주제]
# Gaussian Blur는 주변 픽셀을 단순 평균내는 것이 아니라, 중심 픽셀에 가까운 값에 더 큰 가중치를 주는 블러임
#
# 평균 블러보다 자연스러운 흐림 효과를 만들며, Edge 검출 전 노이즈 제거에 많이 사용됨
#
# [실습 목표]
# 1. Gaussian Blur 개념 이해
# 2. cv2.GaussianBlur() 사용법 이해
# 3. 커널 크기와 sigma 값 이해
# 4. Canny Edge 전처리와의 관계 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. Gaussian 커널 크기를 짝수로 넣음
#
# Gaussian Blur의 커널 크기는 보통 양의 홀수여야 함
#
# 올바른 예:
#
# cv2.GaussianBlur(image, (5, 5), 0)
#
# 잘못된 예:
#
# cv2.GaussianBlur(image, (4, 4), 0)
#
# 실수 2. 무조건 Gaussian Blur가 평균 블러보다 좋다고 생각함
#
# Gaussian Blur는 자연스럽고 안정적이지만, 모든 상황에서 최고의 선택은 아님
#
# 일반 노이즈 완화: Gaussian Blur
# Salt & Pepper 노이즈: Median Blur
# Edge 보존 필요: Bilateral Filter
#
# [ROS2와 연결되는 포인트]
# Canny Edge 검출 전에는 보통 Gaussian Blur를 먼저 적용
#
# 카메라 프레임
# → Grayscale
# → Gaussian Blur
# → Canny Edge
# → Contour 또는 라인 검출
#
# 노이즈가 많은 상태에서 바로 Canny를 적용하면 작은 점까지 Edge로 검출될 수 있음
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
    # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
    gaussian_3 = cv2.GaussianBlur(image, (3, 3), 0)
    gaussian_7 = cv2.GaussianBlur(image, (7, 7), 0)
    gaussian_15 = cv2.GaussianBlur(image, (15, 15), 0)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Gaussian Blur 3x3", gaussian_3)
    cv2.imshow("Gaussian Blur 7x7", gaussian_7)
    cv2.imshow("Gaussian Blur 15x15", gaussian_15)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
