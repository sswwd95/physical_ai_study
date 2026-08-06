# ============================================================================
# 노션 원문 학습 설명: 예제 13. BGR에서 HSV 변환
# ============================================================================
#
# [핵심 주제]
# BGR 이미지를 HSV 색상 공간으로 변환
#
# HSV는 색상 검출에서 매우 중요
#
# H = Hue        색상
# S = Saturation 채도
# V = Value      밝기
#
# OpenCV에서 빨간색, 파란색, 초록색 같은 객체를 검출할 때는 BGR보다 HSV가 훨씬 편리함
#
# [실습 목표]
# 1. HSV 색상 공간 이해
# 2. BGR 이미지를 HSV로 변환
# 3. H, S, V 채널 의미 이해
# 4. 색상 기반 객체 검출 준비
#
# [실무에서 자주 하는 실수]
# 실수 1. Hue 범위를 0~360으로 생각함
#
# OpenCV에서는 Hue가 다음 범위임
#
# 0 ~ 179
#
# 그래서 빨간색, 파란색, 초록색 범위를 지정할 때 이 점을 반드시 기억필요
#
# 실수 2. HSV 이미지를 그대로 저장하거나 표시하고 색이 이상하다고 생각함
#
# HSV 이미지는 사람이 직접 보기 위한 이미지라기보다 색상 검출 계산을 위한 이미지임
#
# [ROS2와 연결되는 포인트]
# ROS2 로봇 비전에서 HSV는 다음 작업에 자주 사용됨
#
# 1. 특정 색상의 공 추적
# 2. 라인트레이싱용 색상 라인 검출
# 3. 컨베이어 위 제품 색상 분류
# 4. 표식 Marker 색상 검출
# 5. 장애물 색상 기반 인식
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/sample.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
bgr_image = cv2.imread(image_path)

# 이미지 또는 검출 결과 생성 여부 확인
if bgr_image is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # 색상 검출이 쉬운 HSV 색상 공간으로 변환
    hsv_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2HSV)

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("BGR 이미지 shape:", bgr_image.shape)
    print("HSV 이미지 shape:", hsv_image.shape)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("BGR Image", bgr_image)
    cv2.imshow("HSV Image", hsv_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
