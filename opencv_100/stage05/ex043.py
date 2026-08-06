# ============================================================================
# 노션 원문 학습 설명: 예제 43. Canny Edge
# ============================================================================
#
# [핵심 주제]
# Canny Edge는 OpenCV에서 가장 많이 사용되는 Edge 검출 방법 중 하나임
#
# Canny는 잡음 제거, 밝기 변화 계산, 얇은 Edge 추출, 임계값 처리를 포함한 실용적인 Edge 검출 방식임
#
# [실습 목표]
# 1. Canny Edge 개념 이해
# 2. Gaussian Blur 전처리
# 3. cv2.Canny() 사용법 이해
# 4. threshold1, threshold2 의미 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. Canny 임계값을 고정값으로만 사용
#
# 조명과 카메라 환경에 따라 적절한 임계값은 변화
#
# edges = cv2.Canny(blurred, 50, 150)
#
# 이 값은 시작점일 뿐임
#
# 실무에서는 다음 값을 실험함
#
# 30, 100
# 50, 150
# 100, 200
#
# 실수 2. 컬러 이미지에 바로 Canny 적용
#
# Canny는 1채널 이미지에서 사용하는 것이 일반적임
#
# 다음 흐름을 권장함
#
# BGR
# → Grayscale
# → Gaussian Blur
# → Canny
#
# [ROS2와 연결되는 포인트]
# Canny Edge는 ROS2 로봇 비전에서 다음 작업에 많이 사용됨
#
# 1. 라인 후보 검출
# 2. 장애물 외곽선 검출
# 3. 작업물 경계 추출
# 4. Contour 검출 전처리
#
# 특히 다음 예제의 Contour 검출과 자주 연결됨
#
# Canny Edge
# → findContours
# → Bounding Box
# → 중심 좌표 계산
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
    # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 두 개의 임계값을 사용하는 Canny 알고리즘으로 안정적인 경계선을 찾습니다.
    edges = cv2.Canny(blurred, 50, 150)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Blurred Gray", blurred)
    cv2.imshow("Canny Edge", edges)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
