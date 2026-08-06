# ============================================================================
# 노션 원문 학습 설명: 예제 93. ArUco Marker 검출
# ============================================================================
#
# [핵심 주제]
# ArUco Marker는 로봇 비전에서 위치 인식, 마커 기반 정렬, 작업 위치 지정에 자주 사용되는 사각형 마커임
#
# OpenCV의 `aruco` 모듈을 사용하면 마커 ID와 꼭짓점을 검출할 수 있음
#
# [실습 목표]
# 1. ArUco Dictionary 이해
# 2. Marker 검출
# 3. Marker ID 표시
# 4. Marker 중심 좌표 계산
#
# [실무에서 자주 하는 실수]
# 실수 1. opencv-python만 설치하고 aruco가 없다고 당황함
#
# 일부 환경에서는 `opencv-contrib-python`이 필요할 수 있음
#
# pip install opencv-contrib-python
#
# 실수 2. 마커가 너무 작거나 흐림
#
# 마커가 작거나 초점이 흐리면 검출률이 떨어집니다.
#
# 마커는 충분히 크게 출력하고, 카메라 초점을 맞춰야 함
#
# [ROS2와 연결되는 포인트]
# ArUco Marker는 다음 프로젝트에 자주 사용됨
#
# 로봇 정지 위치 지정
# 로봇 팔 Pick 기준점 설정
# 충전 스테이션 위치 인식
# 카메라 캘리브레이션 보조
# 작업대 좌표 기준 마커
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 열기
cap = cv2.VideoCapture(0)

# ArUco 마커 검출과 관련된 OpenCV 기능을 사용
aruco_dict = cv2.aruco.getPredefinedDictionary(
    cv2.aruco.DICT_4X4_50
)

# ArUco 마커 검출과 관련된 OpenCV 기능을 사용
parameters = cv2.aruco.DetectorParameters()

# ArUco 마커 검출과 관련된 OpenCV 기능을 사용
detector = cv2.aruco.ArucoDetector(
    aruco_dict,
    parameters
)

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

        # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        corners, ids, rejected = detector.detectMarkers(gray)

        # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
        if ids is not None:
            # ArUco 마커 검출과 관련된 OpenCV 기능을 사용
            cv2.aruco.drawDetectedMarkers(frame, corners, ids)

            # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
            for marker_corners, marker_id in zip(corners, ids):
                # points 변수에 이후 처리에 사용할 값을 저장
                points = marker_corners[0]

                # center x 값을 계산하거나 저장해 이후 처리에서 사용
                center_x = int(points[:, 0].mean())
                # center y 값을 계산하거나 저장해 이후 처리에서 사용
                center_y = int(points[:, 1].mean())

                # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                cv2.circle(
                    frame,
                    (center_x, center_y),
                    6,
                    (0, 0, 255),
                    -1
                )

                # 이미지 위에 상태나 좌표 정보를 글자로 표시
                cv2.putText(
                    frame,
                    f"ID: {int(marker_id[0])}",
                    (center_x + 10, center_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.7,
                    (0, 255, 0),
                    2
                )

                # 현재 상태 또는 계산 결과의 터미널 출력
                print("Marker ID:", int(marker_id[0]))
                print("Marker Center:", center_x, center_y)

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("ArUco Detection", frame)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
