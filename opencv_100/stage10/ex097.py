# ============================================================================
# 노션 원문 학습 설명: 예제 97. 컨베이어 객체 카운팅
# ============================================================================
#
# [핵심 주제]
# 컨베이어 위를 지나가는 객체를 검출하고 특정 기준선을 통과할 때 카운트함
#
# 공장 자동화, 물류, 검사 시스템에서 매우 자주 사용되는 구조임
#
# [실습 목표]
# 1. 객체 검출
# 2. 기준선 설정
# 3. 객체 중심점 추적
# 4. 기준선 통과 시 카운트 증가
#
# [실무에서 자주 하는 실수]
# 실수 1. 기준선 근처에서 객체가 여러 프레임 머물며 중복 카운트됨
#
# 영상은 초당 여러 프레임이므로 객체 하나가 기준선 근처에 여러 번 표시
#
# 중복 방지 로직이 필요
#
# 실수 2. 단순 중심점 거리만으로 추적
#
# 실무에서는 객체 ID 추적이 필요
#
# 더 안정적인 방법은 다음임
#
# Centroid Tracking
# SORT
# DeepSORT
# ByteTrack
#
# [ROS2와 연결되는 포인트]
# 컨베이어 카운트 결과는 다음 Topic으로 발행할 수 있음
#
# /vision/object_count
# /vision/object_detected
#
# MES, APS, WMS 시스템과도 연결 가능한 산업용 패턴임
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 열기
cap = cv2.VideoCapture(0)

# count 값을 계산하거나 저장해 이후 처리에서 사용
count = 0
# counted centers 값을 계산하거나 저장해 이후 처리에서 사용
counted_centers = []

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

        # line y 변수에 이후 처리에 사용할 값을 저장
        line_y = height // 2

        # 색상 검출이 쉬운 HSV 색상 공간으로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

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

        # 기준선이나 검출 결과를 표시하기 위해 선을 그리기
        cv2.line(
            frame,
            (0, line_y),
            (width, line_y),
            (255, 0, 0),
            2
        )

        # current centers 값을 계산하거나 저장해 이후 처리에서 사용
        current_centers = []

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

                current_centers.append((center_x, center_y))

                # 검출 영역을 알아보기 쉽도록 사각형을 그리기
                cv2.rectangle(
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    2
                )

                # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                cv2.circle(
                    frame,
                    (center_x, center_y),
                    5,
                    (0, 0, 255),
                    -1
                )

                # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
                if abs(center_y - line_y) < 10:
                    # already counted 값을 계산하거나 저장해 이후 처리에서 사용
                    already_counted = False

                    # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
                    for old_center in counted_centers:
                        old_x, old_y = old_center

                        # distance 변수에 이후 처리에 사용할 값을 저장
                        distance = ((center_x - old_x) ** 2 + (center_y - old_y) ** 2) ** 0.5

                        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
                        if distance < 50:
                            # already counted 값을 계산하거나 저장해 이후 처리에서 사용
                            already_counted = True
                            # 현재 반복문을 즉시 종료
                            break

                    # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
                    if not already_counted:
                        count += 1
                        counted_centers.append((center_x, center_y))
                        # 현재 상태 또는 계산 결과의 터미널 출력
                        print("객체 카운트:", count)

        # 이미지 위에 상태나 좌표 정보를 글자로 표시
        cv2.putText(
            frame,
            f"Count: {count}",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 255, 255),
            2
        )

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Conveyor Counting", frame)
        cv2.imshow("Mask", mask)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
