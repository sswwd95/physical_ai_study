# ============================================================================
# 노션 원문 학습 설명: 예제 68. 색상 객체 Bounding Box
# ============================================================================
#
# [핵심 주제]
# 색상 마스크에서 검출된 객체에 Bounding Box를 그리기
#
# Bounding Box는 객체의 위치와 크기를 간단하게 표현하는 데 매우 유용
#
# [실습 목표]
# 1. 색상 마스크 생성
# 2. Contour 검출
# 3. Bounding Box 계산
# 4. 중심 좌표와 크기 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. Bounding Box 중심과 Contour 중심을 혼동함
#
# Bounding Box 중심은 박스 기준 중심임
#
# center_x = x + w // 2
# center_y = y + h // 2
#
# Contour 중심은 실제 객체 모양의 무게중심에 가깝습니다.
#
# moments = cv2.moments(contour)
#
# 객체가 기울어져 있거나 불규칙하면 두 중심이 다를 수 있음
#
# 실수 2. 여러 객체가 있을 때 모든 박스를 목표로 사용함
#
# 추적 대상이 하나라면 가장 큰 객체만 선택하는 것이 더 안정적임
#
# [ROS2와 연결되는 포인트]
# Bounding Box는 ROS2 비전 메시지로 표현하기 좋습니다.
#
# class_id
# x
# y
# width
# height
# center_x
# center_y
# area
#
# 이 구조는 YOLO 같은 딥러닝 검출 결과와도 비슷함
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
        lower_green = np.array([40, 80, 80])
        upper_green = np.array([80, 255, 255])

        # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성
        mask = cv2.inRange(hsv, lower_green, upper_green)

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

                # 이미지 위에 상태나 좌표 정보를 글자로 표시
                cv2.putText(
                    frame,
                    f"x:{x} y:{y} w:{w} h:{h}",
                    (x, y - 10),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 255, 0),
                    2
                )

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Color Bounding Box", frame)
        cv2.imshow("Mask", mask)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
