# ============================================================================
# 노션 원문 학습 설명: 예제 16. 이미지 대비 조절
# ============================================================================
#
# [핵심 주제]
# 이미지의 대비를 조절함
#
# 대비는 밝은 부분과 어두운 부분의 차이를 의미함
#
# 대비가 낮음: 전체적으로 흐릿함
# 대비가 높음: 밝고 어두운 차이가 뚜렷함
#
# [실습 목표]
# 1. 대비 개념 이해
# 2. alpha 값으로 대비 조절
# 3. convertScaleAbs() 재사용
# 4. 밝기와 대비 차이 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. alpha 값을 너무 크게 설정
#
# 예를 들어 다음처럼 하면 이미지가 과도하게 밝아지고 정보가 사라질 수 있음
#
# high_contrast = cv2.convertScaleAbs(image, alpha=5.0, beta=0)
#
# 실습에서는 보통 다음 범위에서 시작하는 것이 좋습니다.
#
# alpha: 0.8 ~ 2.0
# beta: -50 ~ 50
#
# 실수 2. 대비 조절만으로 모든 문제를 해결하려고 함
#
# 조명 변화가 심한 환경에서는 단순 대비 조절보다 다음 방법이 더 적합할 수 있음
#
# HSV 변환
# Histogram Equalization
# CLAHE
# Adaptive Threshold
# 카메라 노출 고정
# 조명 환경 개선
#
# [ROS2와 연결되는 포인트]
# 로봇 카메라에서 입력 영상이 흐릿하거나 라인과 바닥의 차이가 약할 때 대비 조절을 사용 가능
#
# 예를 들어 라인트레이싱에서는 다음 흐름을 사용 가능
#
# 카메라 이미지
# → Grayscale
# → 대비 조절
# → Threshold
# → 라인 검출
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
    # 픽셀값이 0~255 범위를 벗어나지 않도록 안전하게 밝기·대비를 조절함
    low_contrast = cv2.convertScaleAbs(image, alpha=0.5, beta=0)
    high_contrast = cv2.convertScaleAbs(image, alpha=1.8, beta=0)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Low Contrast", low_contrast)
    cv2.imshow("High Contrast", high_contrast)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
