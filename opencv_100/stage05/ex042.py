# ============================================================================
# 노션 원문 학습 설명: 예제 42. Laplacian Edge
# ============================================================================
#
# [핵심 주제]
# Laplacian Edge는 x방향과 y방향의 변화량을 한 번에 계산하여 Edge를 검출
#
# Sobel이 방향별 Edge를 따로 볼 수 있다면, Laplacian은 전체 경계 변화를 한 번에 강조함
#
# [실습 목표]
# 1. Laplacian Edge 개념 이해
# 2. Grayscale 변환
# 3. Gaussian Blur 후 Edge 검출
# 4. 출력 가능한 형태로 변환
#
# [실무에서 자주 하는 실수]
# 실수 1. Blur 없이 Laplacian 적용
#
# Laplacian은 작은 잡음도 강하게 반응할 수 있음
#
# 실무에서는 보통 다음 흐름이 좋습니다.
#
# Grayscale
# → Gaussian Blur
# → Laplacian
#
# 실수 2. Sobel과 Laplacian의 차이를 모름
#
# | 구분 | 특징 |
# | --- | --- |
# | Sobel | x/y 방향 Edge를 따로 볼 수 있음 |
# | Laplacian | 전체 방향의 Edge를 한 번에 강조 |
# | Canny | 실제 실무에서 가장 널리 쓰이는 Edge 검출 |
#
# [ROS2와 연결되는 포인트]
# Laplacian은 객체 외곽선 강조나 영상 선명도 확인에 사용 가능
#
# 예를 들어 카메라 초점이 맞지 않으면 Edge가 약하게 출력
#
# Laplacian 결과를 이용해 초점 상태를 간단히 평가하는 방식도 가능
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

    # 여러 방향의 급격한 밝기 변화를 이용해 경계선을 찾습니다.
    laplacian = cv2.Laplacian(blurred, cv2.CV_64F)

    # 픽셀값이 0~255 범위를 벗어나지 않도록 안전하게 밝기·대비를 조절함
    laplacian_abs = cv2.convertScaleAbs(laplacian)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Gray Image", gray)
    cv2.imshow("Blurred Image", blurred)
    cv2.imshow("Laplacian Edge", laplacian_abs)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
