# ============================================================================
# 노션 원문 학습 설명: 예제 12. BGR에서 Grayscale 변환
# ============================================================================
#
# [핵심 주제]
# 컬러 이미지를 흑백 이미지로 변환
#
# 흑백 이미지는 색상 정보는 없지만 밝기 정보만 남습니다.
#
# 로봇 비전에서는 흑백 이미지가 매우 자주 사용됨
#
# Edge 검출
# Threshold 이진화
# 라인 트레이싱
# Contour 검출
# SLAM 전처리
#
# [실습 목표]
# 1. 컬러 이미지를 흑백으로 변환
# 2. Grayscale 이미지 구조 이해
# 3. 컬러 이미지와 흑백 이미지의 shape 차이 확인
# 4. 전처리에서 흑백 변환이 필요한 이유 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. 흑백 이미지에 BGR 색상 처리를 적용함
#
# 다음 코드는 흑백 이미지에는 적합하지 않습니다.
#
# hsv = cv2.cvtColor(gray_image, cv2.COLOR_BGR2HSV)
#
# 흑백 이미지는 BGR 3채널이 아니기 때문임
#
# 실수 2. shape를 무조건 3개로 받음
#
# 컬러 이미지는 다음처럼 받을 수 있음
#
# height, width, channels = bgr_image.shape
#
# 하지만 흑백 이미지는 다음처럼 필요
#
# height, width = gray_image.shape
#
# [ROS2와 연결되는 포인트]
# ROS2 카메라 영상에서 계산량을 줄이고 싶을 때 Grayscale 변환을 자주 사용
#
# 예를 들어 라인트레이싱에서는 색상보다 밝기 차이가 중요
#
# 카메라 프레임
# → Grayscale
# → Threshold
# → 라인 영역 검출
# → 중심점 계산
# → /cmd_vel 제어
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
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    gray_image = cv2.cvtColor(bgr_image, cv2.COLOR_BGR2GRAY)

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("컬러 이미지 shape:", bgr_image.shape)
    print("흑백 이미지 shape:", gray_image.shape)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("BGR Image", bgr_image)
    cv2.imshow("Gray Image", gray_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
