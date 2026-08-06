# ============================================================================
# 노션 원문 학습 설명: 예제 98. 로봇 팔 Pick 위치 계산
# ============================================================================
#
# [핵심 주제]
# 로봇 팔이 물체를 집으려면 이미지 좌표를 작업대 좌표로 변환필요
#
# 이번 예제에서는 가장 단순한 선형 스케일 변환으로 개념을 이해함
#
# 실제 현장에서는 Homography 또는 Hand-eye Calibration이 필요
#
# [실습 목표]
# 1. 픽셀 좌표와 로봇 좌표 차이 이해
# 2. 작업대 영역 기준 변환
# 3. 이미지 중심 좌표를 mm 단위로 근사 변환
# 4. Pick 좌표 생성
#
# [실무에서 자주 하는 실수]
# 실수 1. 단순 비례 변환을 실제 로봇에 그대로 사용
#
# 이 예제는 개념 설명용임
#
# 실제 로봇 팔에는 다음이 필요
#
# 카메라 내부 파라미터
# 렌즈 왜곡 보정
# 작업대 평면 Homography
# 카메라 좌표계와 로봇 좌표계 변환
# Hand-eye Calibration
# 로봇 TCP 보정
#
# 실수 2. z좌표를 고려하지 않음
#
# Pick 작업에는 x, y뿐 아니라 z좌표와 그리퍼 자세도 필요
#
# [ROS2와 연결되는 포인트]
# Pick 좌표는 다음 Topic 또는 Action으로 연결됨
#
# /vision/pick_pose
# → 로봇 팔 planning node
# → MoveIt2
# → trajectory 실행
#
# 정식 구조에서는 `geometry_msgs/PoseStamped`를 사용하는 것이 좋습니다.
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
    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    height, width = image.shape[:2]

    # workspace width mm 값을 계산하거나 저장해 이후 처리에서 사용
    workspace_width_mm = 400
    # workspace height mm 값을 계산하거나 저장해 이후 처리에서 사용
    workspace_height_mm = 300

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

    # 검출되거나 매칭된 항목의 개수를 확인
    if len(contours) > 0:
        # 윤곽선이 차지하는 픽셀 면적을 계산
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if area > 500:
            # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산
            x, y, w, h = cv2.boundingRect(largest_contour)

            # center x 값을 계산하거나 저장해 이후 처리에서 사용
            center_x = x + w // 2
            # center y 값을 계산하거나 저장해 이후 처리에서 사용
            center_y = y + h // 2

            # robot x mm 변수에 이후 처리에 사용할 값을 저장
            robot_x_mm = center_x / width * workspace_width_mm
            # robot y mm 변수에 이후 처리에 사용할 값을 저장
            robot_y_mm = center_y / height * workspace_height_mm

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
                f"Pick mm: ({robot_x_mm:.1f}, {robot_y_mm:.1f})",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            # 현재 상태 또는 계산 결과의 터미널 출력
            print("픽셀 좌표:", center_x, center_y)
            print("로봇 Pick 좌표 근사 mm:", robot_x_mm, robot_y_mm)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Pick Position", result)
    cv2.imshow("Mask", mask)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
