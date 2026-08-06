# ============================================================================
# 노션 원문 학습 설명: 예제 22. 비율 유지 Resize
# ============================================================================
#
# [핵심 주제]
# 이미지를 줄이거나 키울 때 원본의 가로세로 비율을 유지
#
# 단순히 원하는 크기로 강제 변경하면 이미지가 찌그러질 수 있음
#
# [실습 목표]
# 1. 원본 비율 유지 개념 이해
# 2. 비율 기반 Resize 구현
# 3. width 기준으로 height 자동 계산
# 4. 이미지 왜곡 방지
#
# [실무에서 자주 하는 실수]
# 실수 1. 비율을 유지하지 않고 강제 Resize
#
# 다음처럼 하면 이미지가 찌그러질 수 있음
#
# resized_image = cv2.resize(image, (640, 640))
#
# 원본이 16:9 영상인데 1:1로 바꾸면 사람, 라인, 객체의 형태가 왜곡됨
#
# 실수 2. int 변환을 하지 않음
#
# `cv2.resize()`의 크기 값은 정수여야 합니다.
#
# 다음처럼 실수 값이 들어가면 오류가 날 수 있음
#
# target_height = original_height * ratio
#
# 안전하게 다음처럼 작성함
#
# target_height = int(original_height * ratio)
#
# [ROS2와 연결되는 포인트]
# 딥러닝 모델은 고정 입력 크기를 요구하는 경우가 많습니다.
#
# 예를 들어 YOLO 계열 모델은 보통 다음과 같은 입력 크기를 사용
#
# 640×640
#
# 하지만 카메라 원본이 1280×720이면 비율이 다릅니다.
#
# 무작정 640×640으로 바꾸면 객체가 찌그러집니다.
#
# 이때는 보통 다음 방법을 사용
#
# 1. 비율 유지 Resize
# 2. 부족한 부분 Padding
# 3. 모델 입력 크기 맞춤
#
# 이 방식은 이후 예제 28의 이미지 패딩과 연결됨
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
    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    original_height, original_width = image.shape[:2]

    # target width 값을 계산하거나 저장해 이후 처리에서 사용
    target_width = 320
    # ratio 변수에 이후 처리에 사용할 값을 저장
    ratio = target_width / original_width
    # target height 값을 계산하거나 저장해 이후 처리에서 사용
    target_height = int(original_height * ratio)

    # 이미지의 가로·세로 크기를 원하는 크기로 변경함
    resized_image = cv2.resize(image, (target_width, target_height))

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("원본 크기:", image.shape)
    print("비율 유지 Resize 크기:", resized_image.shape)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Aspect Ratio Resized Image", resized_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
