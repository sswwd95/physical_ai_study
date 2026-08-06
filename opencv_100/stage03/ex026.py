# ============================================================================
# 노션 원문 학습 설명: 예제 26. Affine Transform
# ============================================================================
#
# [핵심 주제]
# Affine Transform은 이미지의 점 3개를 기준으로 이미지를 변형하는 방법임
#
# Affine 변환으로 할 수 있는 대표 작업은 다음과 같습니다.
#
# 이동
# 회전
# 확대/축소
# 기울이기
#
# 단, 평행한 선은 변환 후에도 평행 관계가 유지됨
#
# [실습 목표]
# 1. Affine Transform 개념 이해
# 2. 원본 점 3개 지정
# 3. 변환 후 점 3개 지정
# 4. cv2.getAffineTransform() 사용
# 5. cv2.warpAffine() 적용
#
# [실무에서 자주 하는 실수]
# 실수 1. 점 좌표 개수를 잘못 지정함
#
# Affine Transform은 반드시 원본 점 3개, 결과 점 3개가 필요
#
# src_points = np.float32([[x1, y1], [x2, y2], [x3, y3]])
# dst_points = np.float32([[x1, y1], [x2, y2], [x3, y3]])
#
# 점이 2개 또는 4개이면 Affine 변환에 맞지 않습니다.
#
# 실수 2. 좌표 타입을 float32로 지정하지 않음
#
# OpenCV 변환 함수는 보통 `np.float32` 좌표를 요구함
#
# 다음처럼 작성하는 것이 안전
#
# src_points = np.float32([...])
#
# [ROS2와 연결되는 포인트]
# Affine Transform은 로봇 비전에서 이미지 정렬이나 데이터 증강에 사용 가능
#
# 예를 들어 다음 상황임
#
# 카메라가 약간 기울어진 영상 보정
# 학습 데이터에서 이미지를 조금씩 변형하여 데이터 증가
# 작업물 위치를 정렬해 검사하기
#
# 하지만 바닥을 위에서 내려다보는 것처럼 바꾸는 작업에는 보통 Perspective Transform을 더 많이 사용
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
    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    height, width = image.shape[:2]

    # OpenCV 변환 함수가 요구하는 32비트 실수 형식으로 좌표를 생성
    src_points = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    # OpenCV 변환 함수가 요구하는 32비트 실수 형식으로 좌표를 생성
    dst_points = np.float32([
        [70, 80],
        [220, 50],
        [80, 230]
    ])

    # affine matrix 변수에 이후 처리에 사용할 값을 저장
    affine_matrix = cv2.getAffineTransform(src_points, dst_points)

    # 이동·회전·기울이기 같은 Affine 변환을 이미지에 적용
    affine_image = cv2.warpAffine(image, affine_matrix, (width, height))

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Affine Transform", affine_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
