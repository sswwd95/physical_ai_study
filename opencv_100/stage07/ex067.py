# ============================================================================
# 노션 원문 학습 설명: 예제 67. 실시간 원 검출
# ============================================================================
#
# [핵심 주제]
# 실시간 카메라 영상에서 색상 기반으로 객체를 검출한 뒤, 최소 외접 원을 그리기
#
# 공처럼 둥근 물체를 추적할 때 적합
#
# [실습 목표]
# 1. 색상 마스크 생성
# 2. Contour 검출
# 3. 최소 외접 원 계산
# 4. 중심점과 반지름 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. 원형이 아닌 객체에도 외접 원을 사용함
#
# 사각형 물체에도 외접 원은 그릴 수 있지만, 실제 모양을 잘 표현하지 못함
#
# 원형 객체에는 외접 원이 좋고, 일반 객체에는 Bounding Box가 더 좋습니다.
#
# 실수 2. 반지름을 거리로 바로 변환함
#
# 반지름이 크면 가까운 것은 맞지만, 실제 거리로 바꾸려면 카메라 캘리브레이션과 객체 실제 크기 정보가 필요
#
# [ROS2와 연결되는 포인트]
# 공 추적 로봇에서는 다음 값을 발행할 수 있음
#
# center_x
# center_y
# radius
#
# 이 중 `radius`는 접근/정지 판단에 활용할 수 있음
#
# radius가 작음 → 멀리 있음 → 전진
# radius가 큼 → 가까움 → 정지
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
        contours, hierarchy = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # 검출되거나 매칭된 항목의 개수를 확인
        if len(contours) > 0:
            # 윤곽선이 차지하는 픽셀 면적을 계산
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
            if area > 500:
                # 윤곽선을 모두 포함하는 가장 작은 원의 중심과 반지름을 구함
                (x, y), radius = cv2.minEnclosingCircle(largest_contour)

                # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
                if radius > 10:
                    # center 값을 계산하거나 저장해 이후 처리에서 사용
                    center = (int(x), int(y))
                    # radius 값을 계산하거나 저장해 이후 처리에서 사용
                    radius = int(radius)

                    # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                    cv2.circle(
                        frame,
                        center,
                        radius,
                        (0, 255, 255),
                        2
                    )

                    # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                    cv2.circle(
                        frame,
                        center,
                        5,
                        (0, 0, 255),
                        -1
                    )

                    # 이미지 위에 상태나 좌표 정보를 글자로 표시
                    cv2.putText(
                        frame,
                        f"Radius: {radius}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2
                    )

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Circle Tracking", frame)
        cv2.imshow("Mask", mask)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
