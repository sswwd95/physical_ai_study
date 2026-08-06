# ============================================================================
# 노션 원문 학습 설명: 예제 69. 여러 객체 추적
# ============================================================================
#
# [핵심 주제]
# 색상 마스크에서 여러 객체를 동시에 검출하고 각각의 중심과 Bounding Box를 표시
#
# [실습 목표]
# 1. 여러 Contour 처리
# 2. 면적 기준 필터링
# 3. 객체 번호 표시
# 4. 여러 객체 중심점 계산
#
# [실무에서 자주 하는 실수]
# 실수 1. object_id가 진짜 추적 ID라고 생각함
#
# 이 예제의 `object_id`는 현재 프레임에서 순서대로 붙인 번호임
#
# 다음 프레임에서도 같은 객체가 같은 ID를 유지한다는 보장은 없음
#
# 진짜 객체 추적 ID를 유지하려면 다음 기술이 필요
#
# 이전 프레임 중심점과 현재 프레임 중심점 매칭
# Kalman Filter
# SORT
# DeepSORT
# ByteTrack
#
# 실수 2. Contour 순서를 신뢰함
#
# `findContours()`가 반환하는 순서는 항상 원하는 정렬 순서가 아닙니다.
#
# 필요하면 면적 기준으로 정렬함
#
# contours = sorted(contours, key=cv2.contourArea, reverse=True)
#
# [ROS2와 연결되는 포인트]
# 여러 객체를 ROS2로 보낼 때는 배열 형태의 메시지가 필요
#
# 예를 들면 다음과 같은 구조임
#
# detected_objects:
# - id
# - center_x
# - center_y
# - width
# - height
# - area
#
# 커스텀 메시지나 `vision_msgs` 계열 메시지로 확장할 수 있음
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

        # 색상 검출이 쉬운 HSV 색상 공간으로 변환
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현함
        lower_blue = np.array([100, 100, 100])
        upper_blue = np.array([130, 255, 255])

        # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
        mask = cv2.inRange(hsv, lower_blue, upper_blue)

        # 형태학적 연산이나 필터에 사용할 값이 1인 커널 배열을 생성
        kernel = np.ones((5, 5), np.uint8)
        # 작은 흰색 노이즈를 제거하기 위해 열기 연산을 적용
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # 객체 내부의 작은 검은 구멍을 메우기 위해 닫기 연산을 적용
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
        contours, hierarchy = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # object id 변수에 이후 처리에 사용할 값을 저장
        object_id = 0

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
                    frame,
                    (x, y),
                    (x + w, y + h),
                    (255, 0, 0),
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

                # 이미지 위에 상태나 좌표 정보를 글자로 표시
                cv2.putText(
                    frame,
                    f"ID:{object_id} Area:{int(area)}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (255, 0, 0),
                    2
                )

                # 현재 상태 또는 계산 결과의 터미널 출력
                print(
                    "ID:",
                    object_id,
                    "Center:",
                    center_x,
                    center_y,
                    "Area:",
                    area
                )

                object_id += 1

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Multi Object Tracking", frame)
        cv2.imshow("Mask", mask)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
