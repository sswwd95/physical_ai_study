# ============================================================================
# 노션 원문 학습 설명: 예제 94. QR 코드 검출
# ============================================================================
#
# [핵심 주제]
# QR 코드는 물체 ID, 작업 지시, 위치 정보, 제품 정보를 담을 수 있음
#
# OpenCV의 `QRCodeDetector`를 사용하면 QR 코드를 검출하고 문자열 데이터를 읽기 가능
#
# [실습 목표]
# 1. QRCodeDetector 사용법 이해
# 2. QR 코드 위치 검출
# 3. QR 데이터 읽기
# 4. QR 영역 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. QR 코드가 검출되었지만 data가 비어 있음
#
# 검출은 되었지만 초점, 조명, 각도 때문에 디코딩은 실패할 수 있음
#
# 마커가 너무 작거나 흐리면 문자열을 읽지 못함
#
# 실수 2. QR을 너무 비스듬히 보여줌
#
# QR 코드는 어느 정도 기울어져도 읽히지만, 너무 비스듬하면 실패함
#
# [ROS2와 연결되는 포인트]
# QR 코드는 다음에 활용할 수 있음
#
# 제품 ID 인식
# 작업 지시 코드 읽기
# 로봇 목적지 정보 읽기
# 물류 박스 식별
# 컨베이어 제품 분류
#
# ROS2에서는 읽은 문자열을 `std_msgs/String` Topic으로 발행할 수 있음
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 열기
cap = cv2.VideoCapture(0)

# 이미지에서 QR 코드를 찾고 내용을 읽는 검출기를 생성
qr_detector = cv2.QRCodeDetector()

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

        data, points, straight_qrcode = qr_detector.detectAndDecode(frame)

        # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
        if points is not None:
            # points 변수에 이후 처리에 사용할 값을 저장
            points = points.astype(int)

            # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
            for i in range(len(points[0])):
                # pt1 변수에 이후 처리에 사용할 값을 저장
                pt1 = tuple(points[0][i])
                # pt2 변수에 이후 처리에 사용할 값을 저장
                pt2 = tuple(points[0][(i + 1) % len(points[0])])

                # 기준선이나 검출 결과를 표시하기 위해 선을 그리기
                cv2.line(
                    frame,
                    pt1,
                    pt2,
                    (0, 255, 0),
                    2
                )

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
            if data:
                # 이미지 위에 상태나 좌표 정보를 글자로 표시
                cv2.putText(
                    frame,
                    data,
                    tuple(points[0][0]),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 0, 255),
                    2
                )

                # 현재 상태 또는 계산 결과의 터미널 출력
                print("QR 데이터:", data)

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("QR Code Detection", frame)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
