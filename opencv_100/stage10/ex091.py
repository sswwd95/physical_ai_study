"""예제 91. 라인 트레이싱 전처리

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

        # roi 변수에 이후 처리에 사용할 값을 저장합니다.
        roi = frame[int(height * 0.6):height, 0:width]

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

        # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
        cv2.imshow("Original Frame", frame)
        cv2.imshow("Line ROI", roi)
        cv2.imshow("Line Binary", binary)

        # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료합니다.
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환합니다.
    cap.release()
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
