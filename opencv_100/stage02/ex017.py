# ============================================================================
# 노션 원문 학습 설명: 예제 17. 이미지 반전
# ============================================================================
#
# [핵심 주제]
# 이미지의 픽셀 값을 반전함
#
# 흑백 이미지 기준으로 보면 다음과 같습니다.
#
# 검정 ↔ 흰색
# 어두운 부분 ↔ 밝은 부분
#
# 컬러 이미지에서는 각 BGR 채널 값이 모두 반전됨
#
# [실습 목표]
# 1. 이미지 반전 개념 이해
# 2. cv2.bitwise_not() 사용법 이해
# 3. 컬러 이미지 반전
# 4. 흑백 이미지 반전
#
# [실무에서 자주 하는 실수]
# 실수 1. 반전 후 Threshold 조건을 그대로 사용함
#
# 예를 들어 원래는 흰색 라인을 찾고 있었는데 이미지를 반전하면 라인이 검정색이 됨
#
# 따라서 Threshold 조건도 바꿔야 함
#
# 실수 2. 반전이 꼭 성능 향상을 의미한다고 생각함
#
# 반전은 상황에 따라 유용하지만 항상 좋은 것은 아님
#
# 예를 들어 검정 라인을 흰색 배경에서 찾을 때 반전하면 라인이 흰색이 되어 이진화가 쉬워질 수 있음
#
# [ROS2와 연결되는 포인트]
# 라인 트레이싱에서 검정색 라인을 추적할 때 반전을 사용하면 처리 흐름이 단순해질 수 있음
#
# 원본 영상
# → Grayscale
# → Threshold
# → 반전
# → 흰색 라인으로 검출
#
# Contour 검출은 보통 흰색 영역을 객체로 보기 때문에, 검정색 객체를 찾을 때 반전이 유용
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

    # 각 픽셀값을 반전하여 밝고 어두운 영역을 서로 바꿉니다.
    inverted_color = cv2.bitwise_not(image)
    inverted_gray = cv2.bitwise_not(gray_image)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Color", image)
    cv2.imshow("Inverted Color", inverted_color)
    cv2.imshow("Original Gray", gray_image)
    cv2.imshow("Inverted Gray", inverted_gray)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
