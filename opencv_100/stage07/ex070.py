# ============================================================================
# 노션 원문 학습 설명: 예제 70. ROS2 Topic 변환 준비
# ============================================================================
#
# [핵심 주제]
# OpenCV에서 계산한 객체 정보를 ROS2 Topic으로 발행할 수 있도록 데이터 구조를 정리함
#
# 이번 예제는 실제 ROS2 코드는 아니지만, ROS2 노드로 옮기기 쉽게 OpenCV 처리 결과를 딕셔너리 형태로 정리함
#
# [실습 목표]
# 1. 객체 검출 결과를 구조화
# 2. 중심 좌표, 면적, 박스 정보 저장
# 3. ROS2 메시지로 변환하기 쉬운 형태 이해
# 4. OpenCV 코드와 ROS2 코드 분리 준비
#
# [실무에서 자주 하는 실수]
# 실수 1. OpenCV 처리 코드와 ROS2 Publisher 코드를 섞어버림
#
# 초보자는 한 함수 안에 다음을 모두 넣는 경우가 많습니다.
#
# 이미지 변환
# 색상 검출
# Contour 계산
# ROS2 메시지 생성
# Publish
# 화면 출력
#
# 이렇게 하면 디버깅이 어려워집니다.
#
# 권장 구조는 다음임
#
# detect_objects(frame)
# → 객체 정보 반환
# ROS2 callback
# → detect_objects 호출
# → 메시지 변환
# → publish
#
# 실수 2. NumPy 타입을 ROS2 메시지에 바로 넣음
#
# OpenCV 결과 중 일부 값은 NumPy 타입일 수 있음
#
# ROS2 메시지에는 Python 기본 타입으로 변환하는 것이 안전
#
# center_x=int(center_x)
# area=float(area)
#
# [ROS2와 연결되는 포인트]
# 이 예제의 `objects` 리스트는 ROS2에서 다음과 같은 메시지로 바꿀 수 있음
#
# center_x: int
# center_y: int
# x: int
# y: int
# width: int
# height: int
# area: float
#
# 간단한 실습에서는 `std_msgs/String`으로 JSON 문자열을 발행할 수도 있음
#
# [
# {
# "center_x":320,
# "center_y":240,
# "x":280,
# "y":200,
# "width":80,
# "height":80,
# "area":5200.0
# }
# ]
#
# 정식 프로젝트에서는 커스텀 메시지를 만드는 것이 좋습니다.
#
# # 7단계 핵심 정리
#
# 이번 7단계에서는 색상 기반 객체 검출과 추적의 핵심 흐름을 배웠습니다.
#
# | 예제 | 핵심 내용 |
# | --- | --- |
# | 61 | HSV 색상 마스크 |
# | 62 | 빨간색 객체 검출 |
# | 63 | 파란색 객체 검출 |
# | 64 | 초록색 객체 검출 |
# | 65 | 마스크 노이즈 제거 |
# | 66 | 객체 중심 추적 |
# | 67 | 실시간 원 검출 |
# | 68 | 색상 객체 Bounding Box |
# | 69 | 여러 객체 추적 |
# | 70 | ROS2 Topic 변환 준비 |
#
# # 초보자가 반드시 기억해야 할 핵심 문법
#
# hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
#
# BGR 이미지를 HSV로 변환
#
# mask = cv2.inRange(hsv, lower_color, upper_color)
#
# 특정 색상 범위만 마스크로 생성
#
# mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
# mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
#
# 마스크 노이즈를 제거
#
# contours, hierarchy = cv2.findContours(
# mask,
# cv2.RETR_EXTERNAL,
# cv2.CHAIN_APPROX_SIMPLE
# )
#
# 마스크에서 외곽선을 찾습니다.
#
# largest_contour = max(contours, key=cv2.contourArea)
#
# 가장 큰 객체를 선택
#
# x, y, w, h = cv2.boundingRect(contour)
#
# Bounding Box를 계산
#
# center_x = x + w // 2
# center_y = y + h // 2
#
# 박스 중심 좌표를 계산
#
# moments = cv2.moments(contour)
# center_x = int(moments["m10"] / moments["m00"])
# center_y = int(moments["m01"] / moments["m00"])
#
# Contour 중심 좌표를 계산
#
# error_x = center_x - image_center_x
#
# 화면 중앙 대비 객체 위치 오차를 계산
#
# objects.append({
# "center_x": center_x,
# "center_y": center_y,
# "x": x,
# "y": y,
# "width": w,
# "height": h,
# "area": area
# })
#
# ROS2 Topic으로 보낼 수 있도록 객체 정보를 구조화함
#
# # ROS2 Humble 강의 전 관점에서 중요한 이유
#
# 이번 단계는 OpenCV에서 ROS2 비전 제어로 넘어가는 핵심임
#
# 카메라 프레임
# → 색상 기반 객체 검출
# → 중심점 계산
# → 화면 중앙 대비 오차 계산
# → ROS2 Topic 발행
# → 주행 제어 또는 로봇 팔 제어
#
# 특히 다음 ROS2 프로젝트의 기반이 됨
#
# 색상 공 추종 로봇
# 라인 트레이싱 로봇
# 색상 마커 기반 위치 추정
# 컨베이어 색상 객체 분류
# 로봇 팔 Pick 위치 검출
#
# # 실무 기준 색상 검출 처리 흐름
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 이미지 배열 및 수치 계산용 NumPy 불러오기
import numpy as np

# detect_blue_objects 작업을 반복해서 사용할 수 있도록 함수로 정의함
def detect_blue_objects(frame):
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

    # objects 변수에 이후 처리에 사용할 값을 저장
    objects = []

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

            # obj 변수에 이후 처리에 사용할 값을 저장
            obj = {
                "center_x": center_x,
                "center_y": center_y,
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "area": area
            }

            objects.append(obj)

    # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
    return objects, mask

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

        objects, mask = detect_blue_objects(frame)

        # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
        for index, obj in enumerate(objects):
            # x 변수에 이후 처리에 사용할 값을 저장
            x = obj["x"]
            # y 변수에 이후 처리에 사용할 값을 저장
            y = obj["y"]
            # w 변수에 이후 처리에 사용할 값을 저장
            w = obj["width"]
            # h 변수에 이후 처리에 사용할 값을 저장
            h = obj["height"]
            # center x 값을 계산하거나 저장해 이후 처리에서 사용
            center_x = obj["center_x"]
            # center y 값을 계산하거나 저장해 이후 처리에서 사용
            center_y = obj["center_y"]
            # area 값을 계산하거나 저장해 이후 처리에서 사용
            area = obj["area"]

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
                f"Obj {index} Area {int(area)}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2
            )

        # 현재 상태 또는 계산 결과의 터미널 출력
        print("ROS2 Topic으로 보낼 객체 목록:", objects)

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("ROS2 Ready Detection", frame)
        cv2.imshow("Mask", mask)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
