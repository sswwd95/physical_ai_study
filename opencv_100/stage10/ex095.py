# ============================================================================
# 노션 원문 학습 설명: 예제 95. 장애물 색상 검출
# ============================================================================
#
# [핵심 주제]
# 로봇이 특정 색상의 장애물을 검출하고 위치를 파악함
#
# 예를 들어 빨간색 장애물을 위험 영역으로 판단할 수 있음
#
# [실습 목표]
# 1. 빨간색 마스크 생성
# 2. 장애물 Contour 검출
# 3. Bounding Box 표시
# 4. 화면 중앙 기준 위치 판단
#
# [실무에서 자주 하는 실수]
# 실수 1. 색상만으로 장애물을 판단함
#
# 빨간 포스터, 빨간 옷, 빨간 조명도 장애물로 검출될 수 있음
#
# 실무에서는 거리 센서, LiDAR, Depth Camera와 함께 판단하는 것이 안전
#
# 실수 2. 면적을 거리로 바로 해석함
#
# 면적이 크면 가까울 가능성이 있지만, 실제 거리는 카메라 보정과 객체 크기를 알아야 계산할 수 있음
#
# [ROS2와 연결되는 포인트]
# 장애물 검출 결과는 다음 Topic으로 발행할 수 있음
#
# /vision/obstacle_detected
# /vision/obstacle_center
# /vision/obstacle_area
#
# 제어 노드는 장애물이 중앙에 크고 가깝게 보이면 정지하도록 만들 수 있음
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

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

        # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
        height, width = frame.shape[:2]
        # image center x 값을 계산하거나 저장해 이후 처리에서 사용
        image_center_x = width // 2

        # 색상 검출이 쉬운 HSV 색상 공간으로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
        lower_red1 = np.array([0, 100, 100])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 100, 100])
        upper_red2 = np.array([179, 255, 255])

        # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

        # mask 변수에 이후 처리에 사용할 값을 저장
        mask = cv2.bitwise_or(mask1, mask2)

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

        # obstacle detected 상태를 참 또는 거짓 값으로 저장
        obstacle_detected = False

        # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
        for contour in contours:
            # 윤곽선이 차지하는 픽셀 면적을 계산
            area = cv2.contourArea(contour)

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
            if area > 800:
                # obstacle detected 상태를 참 또는 거짓 값으로 저장
                obstacle_detected = True

                # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산
                x, y, w, h = cv2.boundingRect(contour)
                # center x 값을 계산하거나 저장해 이후 처리에서 사용
                center_x = x + w // 2
                # center y 값을 계산하거나 저장해 이후 처리에서 사용
                center_y = y + h // 2

                # error x 값을 계산하거나 저장해 이후 처리에서 사용
                error_x = center_x - image_center_x

                # 검출 영역을 알아보기 쉽도록 사각형을 그리기
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 0, 255),
                    2
                )

                # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                cv2.circle(
                    frame,
                    (center_x, center_y),
                    6,
                    (255, 0, 0),
                    -1
                )

                # 이미지 위에 상태나 좌표 정보를 글자로 표시
                cv2.putText(
                    frame,
                    f"Obstacle error_x: {error_x}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

                # 현재 상태 또는 계산 결과의 터미널 출력
                print("장애물 중심:", center_x, center_y, "면적:", area)

        # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
        if not obstacle_detected:
            # 이미지 위에 상태나 좌표 정보를 글자로 표시
            cv2.putText(
                frame,
                "No Red Obstacle",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 0),
                2
            )

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Obstacle Detection", frame)
        cv2.imshow("Obstacle Mask", mask)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
