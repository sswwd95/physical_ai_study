# ============================================================================
# 노션 원문 학습 설명: 예제 91. 라인 트레이싱 전처리
# ============================================================================
#
# [핵심 주제]
# 라인 트레이싱 로봇은 카메라 영상에서 바닥의 선을 찾아 따라가는 로봇임
#
# 전체 이미지를 모두 처리할 필요는 없음
#
# 보통 화면 아래쪽만 보면 충분함
#
# 카메라 프레임
# → 하단 ROI 자르기
# → Grayscale
# → Gaussian Blur
# → Threshold
# → 라인 후보 마스크 생성
#
# [실습 목표]
# 1. 라인 트레이싱용 ROI 설정
# 2. Grayscale 변환
# 3. Threshold 이진화
# 4. 라인 후보 영역 확인
#
# [실무에서 자주 하는 실수]
# 실수 1. 전체 이미지를 모두 처리함
#
# 전체 이미지를 처리하면 벽, 사람, 조명, 책상 다리 같은 불필요한 영역이 검출될 수 있음
#
# 라인 트레이싱은 대부분 하단 ROI만 처리하는 것이 안정적임
#
# 실수 2. Threshold 값을 고정하고 모든 환경에서 사용함
#
# 바닥 색상과 조명에 따라 `100`이라는 기준값은 달라져야 함
#
# 실무에서는 다음 값을 실험함
#
# 80
# 100
# 120
# 150
#
# [ROS2와 연결되는 포인트]
# ROS2 라인 트레이싱 노드는 다음 구조로 확장됨
#
# /camera/image_raw
# → cv_bridge
# → ROI
# → Threshold
# → Contour
# → 라인 중심 계산
# → /cmd_vel 발행
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

        # roi 변수에 이후 처리에 사용할 값을 저장
        roi = frame[int(height * 0.6):height, 0:width]

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

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Line ROI", roi)
        cv2.imshow("Line Binary", binary)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
