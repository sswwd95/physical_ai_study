# ============================================================================
# 노션 원문 학습 설명: 예제 27. Perspective Transform
# ============================================================================
#
# [핵심 주제]
# Perspective Transform은 이미지의 점 4개를 기준으로 시점을 변환하는 방법임
#
# 예를 들어 비스듬히 보이는 바닥 이미지를 위에서 내려다본 것처럼 바꿀 수 있음
#
# 로봇 비전에서는 다음 작업에 매우 중요
#
# 차선 검출
# 라인 트레이싱
# 바닥 좌표 추정
# 작업대 위 물체 위치 계산
# Bird's-eye View 변환
#
# [실습 목표]
# 1. Perspective Transform 개념 이해
# 2. 원본 점 4개 지정
# 3. 변환 후 점 4개 지정
# 4. cv2.getPerspectiveTransform() 사용
# 5. cv2.warpPerspective() 적용
#
# [실무에서 자주 하는 실수]
# 실수 1. 점 순서가 뒤섞임
#
# Perspective Transform에서 점 순서가 매우 중요
#
# 예를 들어 원본 점은 다음 순서인데,
#
# 왼쪽 위 → 오른쪽 위 → 오른쪽 아래 → 왼쪽 아래
#
# 결과 점은 다른 순서로 쓰면 이미지가 꼬이거나 뒤집힙니다.
#
# 실수 2. 원본 좌표가 이미지 범위를 벗어남
#
# 예를 들어 이미지 크기가 640×480인데 다음 좌표를 넣으면 문제가 발생
#
# [800, 600]
#
# 항상 이미지 크기를 확인필요
#
# height, width = image.shape[:2]
#
# [ROS2와 연결되는 포인트]
# Perspective Transform은 ROS2 로봇 주행에서 매우 유용
#
# 예를 들어 카메라가 바닥을 비스듬히 보고 있을 때, 라인은 사다리꼴처럼 보임
#
# 카메라 원본 영상
# → 바닥 영역 4점 선택
# → Perspective Transform
# → 위에서 내려다본 이미지 생성
# → 라인 중심 계산
# → /cmd_vel 제어
#
# 이 방식은 차선 검출, 라인트레이싱, 바닥 마커 검출에서 자주 사용됨
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
    # OpenCV 변환 함수가 요구하는 32비트 실수 형식으로 좌표를 생성
    src_points = np.float32([
        [100, 100],
        [500, 100],
        [550, 400],
        [50, 400]
    ])

    # OpenCV 변환 함수가 요구하는 32비트 실수 형식으로 좌표를 생성
    dst_points = np.float32([
        [0, 0],
        [400, 0],
        [400, 300],
        [0, 300]
    ])

    # 원근 변환에 사용할 3×3 행렬을 계산
    perspective_matrix = cv2.getPerspectiveTransform(src_points, dst_points)

    # 계산한 원근 변환 행렬을 이미지에 적용
    perspective_image = cv2.warpPerspective(image, perspective_matrix, (400, 300))

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Perspective Transform", perspective_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
