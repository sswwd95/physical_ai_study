# ============================================================================
# 노션 원문 학습 설명: 예제 96. 작업물 위치 검출
# ============================================================================
#
# [핵심 주제]
# 작업대 위 물체의 위치를 검출
#
# 로봇 팔 Pick 작업에서는 물체의 중심 좌표가 중요
#
# 작업대 영상
# → 색상 또는 Threshold
# → Contour
# → Bounding Box
# → 중심점 계산
#
# [실습 목표]
# 1. 작업물 후보 영역 검출
# 2. Contour 기반 위치 계산
# 3. 중심점 표시
# 4. Pick 후보 좌표 생성
#
# [실무에서 자주 하는 실수]
# 실수 1. 픽셀 좌표를 로봇 팔 좌표로 바로 사용
#
# 픽셀 좌표는 이미지 안의 위치임
#
# 로봇 팔이 사용하는 실제 좌표와 다릅니다.
#
# 픽셀 좌표를 로봇 좌표로 바꾸려면 다음이 필요
#
# 카메라 캘리브레이션
# 작업대 평면 기준 Homography
# 카메라-로봇 좌표계 변환
# Hand-eye calibration
#
# 실수 2. 그림자까지 작업물로 검출
#
# 조명 조건이 나쁘면 그림자나 반사가 같이 검출될 수 있음
#
# HSV 범위, Morphology, 면적 필터링을 조정필요
#
# [ROS2와 연결되는 포인트]
# 작업물 중심 좌표는 다음 Topic으로 발행할 수 있음
#
# /vision/pick_candidate
#
# 로봇 팔 제어 노드는 이 좌표를 받아 실제 Pick 좌표로 변환
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/workpiece.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
image = cv2.imread(image_path)

# 이미지 또는 검출 결과 생성 여부 확인
if image is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # 색상 검출이 쉬운 HSV 색상 공간으로 변환
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
    lower_object = np.array([20, 80, 80])
    upper_object = np.array([40, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
    mask = cv2.inRange(hsv, lower_object, upper_object)

    # 형태학적 연산이나 필터에 사용할 값이 1인 커널 배열을 생성
    kernel = np.ones((5, 5), np.uint8)
    # 작은 흰색 노이즈를 제거하기 위해 열기 연산을 적용
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # 객체 내부의 작은 검은 구멍을 메우기 위해 닫기 연산을 적용
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 생성
    result = image.copy()

    # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
    for contour in contours:
        # 윤곽선이 차지하는 픽셀 면적을 계산
        area = cv2.contourArea(contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if area > 500:
            # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산
            x, y, w, h = cv2.boundingRect(contour)

            # center x 값을 계산하거나 저장해 이후 처리에서 사용
            center_x = x + w // 2
            # center y 값을 계산하거나 저장해 이후 처리에서 사용
            center_y = y + h // 2

            # 검출 영역을 알아보기 쉽도록 사각형을 그리기
            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
            cv2.circle(
                result,
                (center_x, center_y),
                6,
                (0, 0, 255),
                -1
            )

            # 이미지 위에 상태나 좌표 정보를 글자로 표시
            cv2.putText(
                result,
                f"Pick: ({center_x}, {center_y})",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

            # 현재 상태 또는 계산 결과의 터미널 출력
            print("작업물 중심 픽셀 좌표:", center_x, center_y)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Workpiece Mask", mask)
    cv2.imshow("Workpiece Detection", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
