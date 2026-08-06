"""예제 94. QR 코드 검출

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

# 이미지에서 QR 코드를 찾고 내용을 읽는 검출기를 만듭니다.
qr_detector = cv2.QRCodeDetector()

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

        data, points, straight_qrcode = qr_detector.detectAndDecode(frame)

        # 필요한 조건이 충족되지 않았을 때의 처리를 시작합니다.
        if points is not None:
            # points 변수에 이후 처리에 사용할 값을 저장합니다.
            points = points.astype(int)

            # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복합니다.
            for i in range(len(points[0])):
                # pt1 변수에 이후 처리에 사용할 값을 저장합니다.
                pt1 = tuple(points[0][i])
                # pt2 변수에 이후 처리에 사용할 값을 저장합니다.
                pt2 = tuple(points[0][(i + 1) % len(points[0])])

                # 기준선이나 검출 결과를 표시하기 위해 선을 그립니다.
                cv2.line(
                    frame,
                    pt1,
                    pt2,
                    (0, 255, 0),
                    2
                )

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
            if data:
                # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
                cv2.putText(
                    frame,
                    data,
                    tuple(points[0][0]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

                # 현재 상태나 계산 결과를 터미널에 출력합니다.
                print("QR 데이터:", data)

        # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
        cv2.imshow("QR Code Detection", frame)

        # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료합니다.
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환합니다.
    cap.release()
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
