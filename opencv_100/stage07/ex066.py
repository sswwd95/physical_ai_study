# ============================================================================
# 노션 원문 학습 설명: 예제 66. 객체 중심 추적
# ============================================================================
#
# [핵심 주제]
# 색상 마스크에서 Contour를 찾고, 가장 큰 객체의 중심 좌표를 계산
#
# 이 예제는 색상 기반 객체 추적의 핵심임
#
# [실습 목표]
# 1. 색상 마스크 생성
# 2. Contour 검출
# 3. 가장 큰 Contour 선택
# 4. 중심 좌표 계산
# 5. 화면 중앙 대비 오차 계산
#
# [실무에서 자주 하는 실수]
# 실수 1. 가장 큰 Contour가 항상 목표 객체라고 가정함
#
# 배경에 같은 색의 큰 영역이 있으면 잘못 추적할 수 있음
#
# 실무에서는 다음 조건을 함께 봅니다.
#
# 면적
# 위치
# 가로세로 비율
# ROI 영역
# 이전 프레임 위치
# 움직임 연속성
#
# 실수 2. error_x를 바로 로봇 속도로 사용함
#
# `error_x`는 픽셀 단위입니다.
#
# 로봇 회전 속도로 바꾸려면 적절한 비례 계수가 필요
#
# angular_z = -0.002 * error_x
#
# 단, 실제 로봇에서는 최대 속도 제한을 반드시 적용필요
#
# [ROS2와 연결되는 포인트]
# 이 예제는 ROS2 객체 추적 노드의 핵심 로직임
#
# center_x, center_y, error_x
#
# 이 값을 ROS2 메시지로 발행하면 주행 제어 노드에서 사용 가능
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

        # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
        height, width = frame.shape[:2]
        # image center x 값을 계산하거나 저장해 이후 처리에서 사용
        image_center_x = width // 2

        # 기준선이나 검출 결과를 표시하기 위해 선을 그리기
        cv2.line(
            frame,
            (image_center_x, 0),
            (image_center_x, height),
            (255, 0, 0),
            2
        )

        # 검출되거나 매칭된 항목의 개수를 확인
        if len(contours) > 0:
            # 윤곽선이 차지하는 픽셀 면적을 계산
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
            if area > 500:
                # 윤곽선의 면적과 중심점을 계산하는 데 필요한 모멘트 값을 구함
                moments = cv2.moments(largest_contour)

                # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
                if moments["m00"] != 0:
                    # center x 값을 계산하거나 저장해 이후 처리에서 사용
                    center_x = int(moments["m10"] / moments["m00"])
                    # center y 값을 계산하거나 저장해 이후 처리에서 사용
                    center_y = int(moments["m01"] / moments["m00"])

                    # error x 값을 계산하거나 저장해 이후 처리에서 사용
                    error_x = center_x - image_center_x

                    # 검출한 윤곽선을 결과 이미지 위에 그리기
                    cv2.drawContours(
                        frame,
                        [largest_contour],
                        -1,
                        (0, 255, 0),
                        2
                    )

                    # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                    cv2.circle(
                        frame,
                        (center_x, center_y),
                        8,
                        (0, 0, 255),
                        -1
                    )

                    # 이미지 위에 상태나 좌표 정보를 글자로 표시
                    cv2.putText(
                        frame,
                        f"Center: ({center_x}, {center_y})",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 0, 255),
                        2
                    )

                    # 이미지 위에 상태나 좌표 정보를 글자로 표시
                    cv2.putText(
                        frame,
                        f"Error X: {error_x}",
                        (20, 70),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2
                    )

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Object Tracking", frame)
        cv2.imshow("Mask", mask)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
