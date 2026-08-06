"""예제 67. 실시간 원 검출

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
# 이미지 배열과 수치 계산을 위해 NumPy를 np라는 이름으로 불러옵니다.
import numpy as np

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

        # 색상 검출이 쉬운 HSV 색상 공간으로 변환합니다.
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현합니다.
        lower_red1 = np.array([0, 100, 100])
        upper_red1 = np.array([10, 255, 255])
        lower_red2 = np.array([170, 100, 100])
        upper_red2 = np.array([179, 255, 255])

        # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성합니다.
        mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
        mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
        # mask 변수에 이후 처리에 사용할 값을 저장합니다.
        mask = cv2.bitwise_or(mask1, mask2)

        # 형태학적 연산이나 필터에 사용할 값이 1인 커널 배열을 만듭니다.
        kernel = np.ones((5, 5), np.uint8)
        # 작은 흰색 노이즈를 제거하기 위해 열기 연산을 적용합니다.
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
        # 객체 내부의 작은 검은 구멍을 메우기 위해 닫기 연산을 적용합니다.
        mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

        # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
        contours, hierarchy = cv2.findContours(
            mask,
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_SIMPLE
        )

        # 검출되거나 매칭된 항목의 개수를 확인합니다.
        if len(contours) > 0:
            # 윤곽선이 차지하는 픽셀 면적을 계산합니다.
            largest_contour = max(contours, key=cv2.contourArea)
            area = cv2.contourArea(largest_contour)

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
            if area > 500:
                # 윤곽선을 모두 포함하는 가장 작은 원의 중심과 반지름을 구합니다.
                (x, y), radius = cv2.minEnclosingCircle(largest_contour)

                # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
                if radius > 10:
                    # center 값을 계산하거나 저장해 이후 처리에서 사용합니다.
                    center = (int(x), int(y))
                    # radius 값을 계산하거나 저장해 이후 처리에서 사용합니다.
                    radius = int(radius)

                    # 중심점이나 원형 객체를 표시하기 위해 원을 그립니다.
                    cv2.circle(
                        frame,
                        center,
                        radius,
                        (0, 255, 255),
                        2
                    )

                    # 중심점이나 원형 객체를 표시하기 위해 원을 그립니다.
                    cv2.circle(
                        frame,
                        center,
                        5,
                        (0, 0, 255),
                        -1
                    )

                    # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
                    cv2.putText(
                        frame,
                        f"Radius: {radius}",
                        (20, 40),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.7,
                        (0, 255, 255),
                        2
                    )

        # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
        cv2.imshow("Circle Tracking", frame)
        cv2.imshow("Mask", mask)

        # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료합니다.
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환합니다.
    cap.release()
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
