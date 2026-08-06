# ============================================================================
# 노션 원문 학습 설명: 예제 99. OpenCV + YOLO 연계 준비
# ============================================================================
#
# [핵심 주제]
# YOLO 같은 딥러닝 객체 검출 모델을 사용하려면 OpenCV 프레임을 모델 입력 형식에 맞게 전처리필요
#
# 이번 예제는 실제 YOLO 추론이 아니라, YOLO 입력 전처리 구조를 준비함
#
# 일반적인 YOLO 입력은 다음과 같습니다.
#
# BGR frame
# → RGB 변환
# → Resize
# → 정규화
# → Batch 차원 추가
# → 모델 입력
#
# [실습 목표]
# 1. BGR to RGB 변환
# 2. 모델 입력 크기 Resize
# 3. 0~1 정규화
# 4. NCHW 형태 변환
#
# [실무에서 자주 하는 실수]
# 실수 1. BGR/RGB 변환을 빼먹음
#
# 색상 순서가 틀리면 모델 정확도가 떨어질 수 있음
#
# 실수 2. 무조건 640×640으로 찌그러뜨림
#
# 비율을 유지하지 않고 강제 Resize하면 객체 모양이 왜곡됨
#
# 실제 YOLO에서는 Letterbox 전처리를 많이 사용
#
# [ROS2와 연결되는 포인트]
# ROS2 + YOLO 노드는 보통 다음 구조임
#
# /camera/image_raw
# → cv_bridge
# → OpenCV frame
# → YOLO 전처리
# → 모델 추론
# → Bounding Box 결과
# → /vision/detections 발행
# → debug image 발행
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
    # input size 변수에 이후 처리에 사용할 값을 저장
    input_size = 640

    # OpenCV의 BGR 채널 순서를 일반적인 RGB 순서로 바꿉니다.
    rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    # 이미지의 가로·세로 크기를 원하는 크기로 변경함
    resized = cv2.resize(rgb_image, (input_size, input_size))

    # OpenCV 변환 함수가 요구하는 32비트 실수 형식으로 좌표를 생성
    normalized = resized.astype(np.float32) / 255.0

    # chw 변수에 이후 처리에 사용할 값을 저장
    chw = np.transpose(normalized, (2, 0, 1))

    # batch 변수에 이후 처리에 사용할 값을 저장
    batch = np.expand_dims(chw, axis=0)

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("원본 shape:", image.shape)
    print("RGB Resize shape:", resized.shape)
    print("정규화 범위:", normalized.min(), normalized.max())
    print("CHW shape:", chw.shape)
    print("Batch shape:", batch.shape)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original BGR", image)
    cv2.imshow("YOLO Input Preview", cv2.cvtColor(resized, cv2.COLOR_RGB2BGR))

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
