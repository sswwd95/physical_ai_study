# ============================================================================
# 노션 원문 학습 설명: 예제 73. CLAHE
# ============================================================================
#
# [핵심 주제]
# CLAHE는 Contrast Limited Adaptive Histogram Equalization의 약자임
#
# 일반 히스토그램 평활화는 이미지 전체에 같은 방식으로 적용하지만, CLAHE는 작은 영역별로 대비를 조정함
#
# 조명이 고르지 않은 이미지에서 더 안정적임
#
# [실습 목표]
# 1. CLAHE 개념 이해
# 2. cv2.createCLAHE() 사용법 이해
# 3. clipLimit와 tileGridSize 의미 이해
# 4. 일반 평활화와 차이 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. clipLimit를 너무 크게 설정
#
# clipLimit가 너무 크면 노이즈와 작은 밝기 변화가 과도하게 강조될 수 있음
#
# 처음에는 다음 값으로 시작하는 것이 좋습니다.
#
# clipLimit=2.0
#
# 실수 2. 컬러 이미지에 무작정 CLAHE 적용
#
# 컬러 이미지에 CLAHE를 적용하려면 보통 YCrCb 또는 LAB 색상 공간의 밝기 채널에 적용
#
# 초보 단계에서는 Grayscale에 적용하는 방식부터 익히는 것이 좋습니다.
#
# [ROS2와 연결되는 포인트]
# CLAHE는 조명이 불균일한 환경에서 유용
#
# 복도 한쪽은 밝고 한쪽은 어두움
# 공장 조명이 부분적으로 반사됨
# 바닥 일부가 그림자에 가려짐
#
# 이런 상황에서 라인 검출이나 Edge 검출 전처리에 도움이 될 수 있음
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
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 밝기 히스토그램을 고르게 펴서 이미지 대비를 높임
    equalized = cv2.equalizeHist(gray)

    # 작은 영역별로 대비를 높이되 과도한 증폭을 제한하는 CLAHE 객체를 생성
    clahe = cv2.createCLAHE(
        clipLimit=2.0,
        tileGridSize=(8, 8)
    )

    # 생성한 CLAHE 설정을 흑백 이미지에 적용
    clahe_image = clahe.apply(gray)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Gray", gray)
    cv2.imshow("Histogram Equalization", equalized)
    cv2.imshow("CLAHE", clahe_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
