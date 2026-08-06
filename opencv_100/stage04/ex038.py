# ============================================================================
# 노션 원문 학습 설명: 예제 38. Salt & Pepper 노이즈 제거
# ============================================================================
#
# [핵심 주제]
# Salt & Pepper 노이즈는 이미지에 소금과 후추처럼 흰 점과 검은 점이 튀는 노이즈임
#
# 이런 노이즈는 Median Blur로 제거하는 것이 효과적임
#
# [실습 목표]
# 1. Salt & Pepper 노이즈 개념 이해
# 2. 흰 점과 검은 점 노이즈 생성
# 3. Median Blur로 제거
# 4. 제거 전후 비교
#
# [실무에서 자주 하는 실수]
# 실수 1. 평균 블러로 Salt & Pepper 노이즈를 제거하려 함
#
# 평균 블러도 어느 정도 부드럽게 만들지만, 흰 점과 검은 점이 주변으로 퍼질 수 있음
#
# Salt & Pepper 노이즈에는 보통 Median Blur가 더 적합
#
# 실수 2. Median 커널을 너무 크게 설정
#
# 커널이 너무 크면 노이즈는 줄지만 이미지의 디테일도 사라집니다.
#
# 처음에는 다음 정도부터 시작함
#
# cv2.medianBlur(image, 3)
# cv2.medianBlur(image, 5)
#
# [ROS2와 연결되는 포인트]
# 실제 카메라 영상에서 센서 이상, 전송 오류, 압축 문제 등으로 점 형태 노이즈가 생길 수 있음
#
# 특히 Threshold 이후 마스크에 작은 점들이 많이 생기면 Contour 검출 결과가 불안정해집니다.
#
# 카메라 프레임
# → 색상 마스크
# → 작은 점 노이즈 발생
# → Median Blur 또는 Morphology
# → Contour 검출 안정화
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
    # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 생성
    noisy_image = image.copy()

    # noise ratio 변수에 이후 처리에 사용할 값을 저장
    noise_ratio = 0.02
    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    height, width = image.shape[:2]
    # noise count 값을 계산하거나 저장해 이후 처리에서 사용
    noise_count = int(height * width * noise_ratio)

    # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
    for _ in range(noise_count):
        # 실습용 노이즈를 만들기 위해 난수를 생성
        y = np.random.randint(0, height)
        x = np.random.randint(0, width)

        # 실습용 노이즈를 만들기 위해 난수를 생성
        if np.random.rand() < 0.5:
            noisy_image[y, x] = (0, 0, 0)
        # 앞 조건이 거짓일 때의 실행 구간
        else:
            noisy_image[y, x] = (255, 255, 255)

    # 주변 픽셀의 중앙값을 사용해 Salt & Pepper 노이즈를 줄임
    denoised_image = cv2.medianBlur(noisy_image, 5)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Salt and Pepper Noise", noisy_image)
    cv2.imshow("Denoised by Median Blur", denoised_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
