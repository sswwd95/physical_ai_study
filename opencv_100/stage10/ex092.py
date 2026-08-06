# ============================================================================
# 노션 원문 학습 설명: 예제 92. 차선 중심 계산
# ============================================================================
#
# [핵심 주제]
# 라인 트레이싱에서 가장 중요한 값은 라인의 중심 x좌표임
#
# 화면 중앙과 라인 중심의 차이를 계산하면 로봇이 어느 방향으로 회전해야 하는지 알 수 있음
#
# error_x = line_center_x - image_center_x
#
# [실습 목표]
# 1. 라인 Contour 검출
# 2. 가장 큰 라인 영역 선택
# 3. 라인 중심점 계산
# 4. 화면 중앙 대비 오차 계산
#
# [실무에서 자주 하는 실수]
# 실수 1. ROI 좌표 보정을 잊음
#
# ROI에서 계산한 `center_y`는 전체 이미지 기준 좌표가 아님
#
# 전체 이미지 위에 표시하려면 `roi_start_y`를 더필요
#
# 실수 2. error_x 부호를 로봇 제어에 반대로 사용함
#
# 실제 로봇이 반대로 회전하면 제어식의 부호를 바꿔야 함
#
# angular_z = -0.002 * error_x
#
# 또는
#
# angular_z = 0.002 * error_x
#
# 실제 카메라 장착 방향에 따라 변화 가능
#
# [ROS2와 연결되는 포인트]
# 라인 트레이싱 제어 노드는 다음처럼 동작할 수 있음
#
# error_x가 음수 → 왼쪽으로 보정
# error_x가 양수 → 오른쪽으로 보정
# error_x가 0 근처 → 직진
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

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

        # roi start y 변수에 이후 처리에 사용할 값을 저장
        roi_start_y = int(height * 0.6)
        # roi 변수에 이후 처리에 사용할 값을 저장
        roi = frame[roi_start_y:height, 0:width]

        # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 기준값을 이용해 이미지를 흰색과 검은색의 이진 이미지로 분할
        ret, binary = cv2.threshold(
            blurred,
            100,
            255,
            cv2.THRESH_BINARY_INV
        )

        # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
        contours, _ = cv2.findContours(
            binary,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

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
            if area > 300:
                # 윤곽선의 면적과 중심점을 계산하는 데 필요한 모멘트 값을 구함
                moments = cv2.moments(largest_contour)

                # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
                if moments["m00"] != 0:
                    # line center x 값을 계산하거나 저장해 이후 처리에서 사용
                    line_center_x = int(moments["m10"] / moments["m00"])
                    # line center y 값을 계산하거나 저장해 이후 처리에서 사용
                    line_center_y = int(moments["m01"] / moments["m00"])

                    # line center y on frame 값을 계산하거나 저장해 이후 처리에서 사용
                    line_center_y_on_frame = line_center_y + roi_start_y

                    # error x 값을 계산하거나 저장해 이후 처리에서 사용
                    error_x = line_center_x - image_center_x

                    # 검출한 윤곽선을 결과 이미지 위에 그리기
                    cv2.drawContours(
                        roi,
                        [largest_contour],
                        -1,
                        (0, 255, 0),
                        2
                    )

                    # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                    cv2.circle(
                        frame,
                        (line_center_x, line_center_y_on_frame),
                        8,
                        (0, 0, 255),
                        -1
                    )

                    # 이미지 위에 상태나 좌표 정보를 글자로 표시
                    cv2.putText(
                        frame,
                        f"error_x: {error_x}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 255),
                        2
                    )

                    # 현재 상태 또는 계산 결과의 터미널 출력
                    print("라인 중심:", line_center_x, line_center_y_on_frame)
                    print("화면 중앙 대비 오차:", error_x)

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Line Center Frame", frame)
        cv2.imshow("Line Binary", binary)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
