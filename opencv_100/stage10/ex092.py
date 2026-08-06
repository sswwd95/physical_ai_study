"""예제 92. 차선 중심 계산

초보자용 상세 주석판입니다.

읽는 순서:
1. 위에서 아래로 주석을 먼저 읽습니다.
2. 바로 아래 코드가 어떤 작업을 하는지 확인합니다.
3. 실행 후 나타나는 창이나 터미널 결과를 비교합니다.

실행 위치: 이 프로젝트의 opencv_100 폴더
주의: cv2.imshow()가 있는 예제는 화면 창에서 아무 키나 눌러야 종료됩니다.
"""

# OpenCV 기능을 사용하기 위해 cv2 모듈을 불러옵니다.
import cv2

# 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 엽니다.
cap = cv2.VideoCapture(0)

# 카메라나 동영상 입력이 정상적으로 열렸는지 확인합니다.
if not cap.isOpened():
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("카메라를 열 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    # 조건이 참인 동안 아래 코드를 계속 반복합니다.
    while True:
        # 영상에서 프레임 한 장을 읽고, 성공 여부와 이미지 배열을 각각 받습니다.
        ret, frame = cap.read()

        # 필요한 조건이 충족되지 않았을 때의 처리를 시작합니다.
        if not ret:
            # 현재 상태나 계산 결과를 터미널에 출력합니다.
            print("프레임을 읽을 수 없습니다.")
            # 현재 반복문을 즉시 종료합니다.
            break

        # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
        height, width = frame.shape[:2]
        # image center x 값을 계산하거나 저장해 이후 처리에서 사용합니다.
        image_center_x = width // 2

        # roi start y 변수에 이후 처리에 사용할 값을 저장합니다.
        roi_start_y = int(height * 0.6)
        # roi 변수에 이후 처리에 사용할 값을 저장합니다.
        roi = frame[roi_start_y:height, 0:width]

        # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
        gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용합니다.
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 기준값을 이용해 이미지를 흰색과 검은색의 이진 이미지로 나눕니다.
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

        # 기준선이나 검출 결과를 표시하기 위해 선을 그립니다.
        cv2.line(
            frame,
            (image_center_x, 0),
            (image_center_x, height),
            (255, 0, 0),
            2
        )

        # 검출되거나 매칭된 항목의 개수를 확인합니다.
        if len(contours) > 0:
            # 윤곽선이 차지하는 픽셀 면적을 계산합니다.
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
            if area > 300:
                # 윤곽선의 면적과 중심점을 계산하는 데 필요한 모멘트 값을 구합니다.
                moments = cv2.moments(largest_contour)

                # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
                if moments["m00"] != 0:
                    # line center x 값을 계산하거나 저장해 이후 처리에서 사용합니다.
                    line_center_x = int(moments["m10"] / moments["m00"])
                    # line center y 값을 계산하거나 저장해 이후 처리에서 사용합니다.
                    line_center_y = int(moments["m01"] / moments["m00"])

                    # line center y on frame 값을 계산하거나 저장해 이후 처리에서 사용합니다.
                    line_center_y_on_frame = line_center_y + roi_start_y

                    # error x 값을 계산하거나 저장해 이후 처리에서 사용합니다.
                    error_x = line_center_x - image_center_x

                    # 검출한 윤곽선을 결과 이미지 위에 그립니다.
                    cv2.drawContours(
                        roi,
                        [largest_contour],
                        -1,
                        (0, 255, 0),
                        2
                    )

                    # 중심점이나 원형 객체를 표시하기 위해 원을 그립니다.
                    cv2.circle(
                        frame,
                        (line_center_x, line_center_y_on_frame),
                        8,
                        (0, 0, 255),
                        -1
                    )

                    # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
                    cv2.putText(
                        frame,
                        f"error_x: {error_x}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.8,
                        (0, 255, 255),
                        2
                    )

                    # 현재 상태나 계산 결과를 터미널에 출력합니다.
                    print("라인 중심:", line_center_x, line_center_y_on_frame)
                    print("화면 중앙 대비 오차:", error_x)

        # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
        cv2.imshow("Line Center Frame", frame)
        cv2.imshow("Line Binary", binary)

        # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료합니다.
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환합니다.
    cap.release()
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
