# ============================================================================
# 노션 원문 학습 설명: 예제 40. 실시간 카메라 블러 처리
# ============================================================================
#
# [핵심 주제]
# 웹캠 영상을 실시간으로 읽고, 각 프레임에 Gaussian Blur를 적용
#
# ROS2 카메라 노드와 거의 같은 구조를 갖는 실습임
#
# [실습 목표]
# 1. cv2.VideoCapture() 기본 사용법 복습
# 2. 실시간 프레임 처리 구조 이해
# 3. Gaussian Blur 실시간 적용
# 4. q 키로 종료하는 구조 구현
#
# [실무에서 자주 하는 실수]
# 실수 1. waitKey(0)을 사용함
#
# 실시간 영상에서는 다음 코드를 쓰면 안 됨
#
# cv2.waitKey(0)
#
# 프레임마다 멈춰버립니다.
#
# 실시간 영상에서는 보통 다음처럼 씁니다.
#
# cv2.waitKey(1)
#
# 실수 2. cap.release()를 빼먹음
#
# 카메라 사용이 끝나면 반드시 해제필요
#
# cap.release()
#
# 실수 3. Docker/WSL2에서 카메라가 바로 열린다고 생각함
#
# Windows 10/11 + Docker 또는 WSL2 환경에서는 카메라 접근이 일반 Python 실행보다 복잡할 수 있음
#
# 실무 교육에서는 다음을 따로 확인필요
#
# Windows 장치 권한
# Docker 장치 매핑
# WSL2 USB 장치 연결
# VcXsrv 또는 GUI 표시 설정
# 카메라 번호 0, 1, 2 테스트
#
# [ROS2와 연결되는 포인트]
# 이 예제는 ROS2 카메라 Subscriber 노드와 매우 비슷함
#
# 일반 OpenCV 구조:
#
# VideoCapture
# → frame 읽기
# → OpenCV 처리
# → imshow
#
# ROS2 구조:
#
# /camera/image_raw Subscribe
# → cv_bridge로 frame 변환
# → OpenCV 처리
# → 결과 Publish 또는 imshow
#
# 즉, 이 예제를 이해하면 이후 ROS2에서 다음 노드를 만들 수 있음
#
# 카메라 이미지 Subscriber
# Gaussian Blur 처리
# Edge 검출
# 객체 중심 좌표 계산
# 처리 결과 이미지 Publisher
#
# # 4단계 핵심 정리
#
# 이번 4단계에서는 필터링과 노이즈 제거를 배웠습니다.
#
# | 예제 | 핵심 내용 |
# | --- | --- |
# | 31 | 평균 블러 |
# | 32 | Gaussian Blur |
# | 33 | Median Blur |
# | 34 | Bilateral Filter |
# | 35 | Sharpening |
# | 36 | 엣지 보존 필터 |
# | 37 | 노이즈 이미지 생성 |
# | 38 | Salt & Pepper 노이즈 제거 |
# | 39 | 스무딩 필터 비교 |
# | 40 | 실시간 카메라 블러 처리 |
#
# # 초보자가 반드시 기억해야 할 핵심 문법
#
# blur = cv2.blur(image, (7, 7))
#
# 평균 블러임
#
# gaussian = cv2.GaussianBlur(image, (7, 7), 0)
#
# Gaussian Blur임
#
# Edge 검출 전처리에 자주 사용
#
# median = cv2.medianBlur(image, 5)
#
# Median Blur임
#
# Salt & Pepper 노이즈 제거에 좋습니다.
#
# bilateral = cv2.bilateralFilter(image, 9, 75, 75)
#
# Bilateral Filter임
#
# 경계를 유지하면서 노이즈를 줄임
#
# kernel = np.array([
# [0, -1, 0],
# [-1, 5, -1],
# [0, -1, 0]
# ])
# sharpened = cv2.filter2D(image, -1, kernel)
#
# 이미지 선명화임
#
# edge_preserved = cv2.edgePreservingFilter(
# image,
# flags=1,
# sigma_s=60,
# sigma_r=0.4
# )
#
# 엣지 보존 필터임
#
# noisy_image = image.astype(np.int16) + noise
# noisy_image = np.clip(noisy_image, 0, 255).astype(np.uint8)
#
# 노이즈 이미지를 안전하게 만드는 방식임
#
# cap = cv2.VideoCapture(0)
# ret, frame = cap.read()
#
# 실시간 카메라 프레임을 읽기
#
# # ROS2 Humble 강의 전 관점에서 중요한 이유
#
# ROS2에서 카메라 영상을 처리할 때 필터링은 거의 필수임
#
# 대표적인 흐름은 다음과 같습니다.
#
# /camera/image_raw
# → cv_bridge
# → OpenCV frame
# → Resize
# → Grayscale 또는 HSV
# → Blur 또는 Median Filter
# → Threshold / Edge / Contour
# → 객체 좌표 계산
# → ROS2 Topic Publish
#
# 특히 다음 작업에서는 필터링이 매우 중요
#
# 라인 트레이싱
# 장애물 색상 검출
# 공 추적
# 작업물 외곽선 검출
# 로봇 팔 Pick 위치 계산
# Visual SLAM 전처리
#
# # 실무 기준 필터 선택표
#
# | 상황 | 추천 처리 |
# | --- | --- |
# | 일반적인 영상 노이즈 완화 | Gaussian Blur |
# | 빠르고 단순한 스무딩 | Average Blur |
# | 흰 점/검은 점 노이즈 제거 | Median Blur |
# | 객체 경계를 유지하고 싶음 | Bilateral Filter |
# | 이미지가 약간 흐림 | Sharpening |
# | 보기 좋은 전처리 이미지 필요 | Edge Preserving Filter |
# | 실시간 주행 제어 | 작은 커널 Gaussian Blur |
# | 정밀 검사 이미지 | Bilateral 또는 Edge Preserving 검토 |
# | Threshold 전에 노이즈가 많음 | Gaussian 또는 Median |
# | Contour가 너무 많이 잡힘 | Blur 후 Threshold 또는 Morphology |
#
# # 실무에서 가장 중요한 판단 기준
#
# 필터링은 “많이 할수록 좋은 것”이 아님
#
# 로봇 비전에서는 항상 다음 균형을 봐야 함
#
# 노이즈 제거가 충분한가?
# 객체 경계가 유지되는가?
# FPS가 충분한가?
# 제어 지연이 커지지 않는가?
# 검출 좌표가 안정적인가?
#
# 초보자는 처음에 다음 조합부터 실습하는 것이 좋습니다.
#
# Grayscale
# → Gaussian Blur
# → Threshold
# → Contour
#
# 색상 기반 검출에서는 다음 조합이 좋습니다.
#
# BGR
# → HSV
# → inRange
# → Median Blur
# → Contour
#
# - 5단계: Edge, Contour, Shape 분석
#
# 이번 단계는 ROS2 Humble 로봇 비전에서 객체의 외곽선, 위치, 크기, 중심점을 계산하기 위한 핵심임
#
# 실제 로봇에서는 단순히 이미지를 보는 것이 아니라 다음 정보를 뽑아야 함
#
# 객체가 어디에 있는가?
# 객체의 크기는 어느 정도인가?
# 라인 중심이 화면의 왼쪽인가 오른쪽인가?
# 장애물 외곽선은 어디인가?
# 로봇 팔이 집어야 할 중심 좌표는 어디인가?
#
# # 5단계: Edge, Contour, Shape 분석
#
# | 번호 | 핵심 주제 |
# | --- | --- |
# | 41 | Sobel Edge |
# | 42 | Laplacian Edge |
# | 43 | Canny Edge |
# | 44 | Contour 검출 |
# | 45 | Contour 면적 계산 |
# | 46 | Bounding Box |
# | 47 | 최소 외접 원 |
# | 48 | 다각형 근사 |
# | 49 | 도형 분류 |
# | 50 | 객체 중심점 계산 |
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 열기
cap = cv2.VideoCapture(0)

# 카메라나 동영상 입력이 정상적으로 열렸는지 확인
if not cap.isOpened():
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("카메라를 열 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # 조건이 참인 동안 아래 코드를 계속 반복
    while True:
        # 영상에서 프레임 한 장을 읽고, 성공 여부와 이미지 배열을 각각 수신
        ret, frame = cap.read()

        # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
        if not ret:
            # 현재 상태 또는 계산 결과의 터미널 출력
            print("프레임을 읽을 수 없습니다.")
            # 현재 반복문을 즉시 종료
            break

        # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
        blurred_frame = cv2.GaussianBlur(frame, (7, 7), 0)

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Original Camera", frame)
        cv2.imshow("Blurred Camera", blurred_frame)

        # 키 입력 대기 및 실시간 영상 갱신
        key = cv2.waitKey(1)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if key == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
