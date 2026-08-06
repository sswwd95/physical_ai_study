# ============================================================================
# 노션 원문 학습 설명: 예제 6. 컬러 이미지와 흑백 이미지 비교
# ============================================================================
#
# [핵심 주제]
# 같은 이미지를 컬러와 흑백으로 읽고 차이를 비교
#
# [실습 목표]
# 1. 컬러 이미지 읽기
# 2. 흑백 이미지 읽기
# 3. shape 차이 확인
# 4. 화면에 나란히 출력
#
# [실무에서 자주 하는 실수]
# 실수 1. 흑백 이미지를 컬러 이미지처럼 처리함
#
# 흑백 이미지는 채널이 없으므로 다음 코드는 오류가 날 수 있음
#
# height, width, channels = gray_image.shape
#
# 흑백 이미지는 다음처럼 작성필요
#
# height, width = gray_image.shape
#
# 실수 2. 흑백 이미지인데 색상 검출을 시도함
#
# HSV 색상 검출은 컬러 이미지에서 필요
#
# 흑백 이미지에는 색상 정보가 없기 때문에 빨간색, 파란색 같은 색상 검출이 불가능
#
# [ROS2와 연결되는 포인트]
# 로봇 비전에서는 모든 처리를 컬러 이미지로 할 필요가 없음
#
# 예를 들어 다음 작업은 흑백 이미지로도 충분함
#
# 1. Edge 검출
# 2. Threshold 이진화
# 3. 라인 트레이싱
# 4. 윤곽선 검출
#
# 흑백 이미지를 사용하면 계산량이 줄어들어 실시간 처리에 유리함
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/sample.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
color_image = cv2.imread(image_path, cv2.IMREAD_COLOR)
gray_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# 이미지 또는 검출 결과 생성 여부 확인
if color_image is None or gray_image is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("컬러 이미지 shape:", color_image.shape)
    print("흑백 이미지 shape:", gray_image.shape)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Color Image", color_image)
    cv2.imshow("Gray Image", gray_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
