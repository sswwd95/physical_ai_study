# ============================================================================
# 노션 원문 학습 설명: 예제 33. Median Blur
# ============================================================================
#
# [핵심 주제]
# Median Blur는 주변 픽셀의 평균이 아니라 중간값을 사용
#
# 특히 Salt & Pepper 노이즈, 즉 이미지에 검은 점과 흰 점이 튀는 노이즈를 제거할 때 매우 유용
#
# [실습 목표]
# 1. Median Blur 개념 이해
# 2. cv2.medianBlur() 사용법 이해
# 3. Salt & Pepper 노이즈 제거 원리 이해
# 4. 평균 블러와 차이 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. 커널 크기를 짝수로 넣음
#
# Median Blur의 커널 크기도 일반적으로 1보다 큰 홀수여야 함
#
# 올바른 예:
#
# median = cv2.medianBlur(image, 5)
#
# 잘못된 예:
#
# median = cv2.medianBlur(image, 4)
#
# 실수 2. 모든 노이즈에 Median Blur만 사용
#
# Median Blur는 점 형태 노이즈에는 강하지만, 일반적인 흐림 보정이나 자연스러운 스무딩에는 Gaussian Blur가 더 적합할 수 있음
#
# [ROS2와 연결되는 포인트]
# 카메라 영상에서 흰 점, 검은 점처럼 튀는 노이즈가 생기면 Median Blur가 효과적임
#
# 특히 다음 작업 전처리에 사용 가능
#
# 1. Threshold 이진화
# 2. 색상 마스크 생성
# 3. Contour 검출
# 4. 라인 검출
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
    # 주변 픽셀의 중앙값을 사용해 Salt & Pepper 노이즈를 줄임
    median_3 = cv2.medianBlur(image, 3)
    median_5 = cv2.medianBlur(image, 5)
    median_9 = cv2.medianBlur(image, 9)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Median Blur 3", median_3)
    cv2.imshow("Median Blur 5", median_5)
    cv2.imshow("Median Blur 9", median_9)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
