"""예제 70. ROS2 Topic 변환 준비

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

# detect_blue_objects 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
def detect_blue_objects(frame):
    # 색상 검출이 쉬운 HSV 색상 공간으로 변환합니다.
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현합니다.
    lower_blue = np.array([100, 100, 100])
    upper_blue = np.array([130, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성합니다.
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

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

    # objects 변수에 이후 처리에 사용할 값을 저장합니다.
    objects = []

    # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복합니다.
    for contour in contours:
        # 윤곽선이 차지하는 픽셀 면적을 계산합니다.
        area = cv2.contourArea(contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
        if area > 500:
            # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산합니다.
            x, y, w, h = cv2.boundingRect(contour)

            # center x 값을 계산하거나 저장해 이후 처리에서 사용합니다.
            center_x = x + w // 2
            # center y 값을 계산하거나 저장해 이후 처리에서 사용합니다.
            center_y = y + h // 2

            # obj 변수에 이후 처리에 사용할 값을 저장합니다.
            obj = {
                "center_x": center_x,
                "center_y": center_y,
                "x": x,
                "y": y,
                "width": w,
                "height": h,
                "area": area
            }

            objects.append(obj)

    # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료합니다.
    return objects, mask

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

        objects, mask = detect_blue_objects(frame)

        # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복합니다.
        for index, obj in enumerate(objects):
            # x 변수에 이후 처리에 사용할 값을 저장합니다.
            x = obj["x"]
            # y 변수에 이후 처리에 사용할 값을 저장합니다.
            y = obj["y"]
            # w 변수에 이후 처리에 사용할 값을 저장합니다.
            w = obj["width"]
            # h 변수에 이후 처리에 사용할 값을 저장합니다.
            h = obj["height"]
            # center x 값을 계산하거나 저장해 이후 처리에서 사용합니다.
            center_x = obj["center_x"]
            # center y 값을 계산하거나 저장해 이후 처리에서 사용합니다.
            center_y = obj["center_y"]
            # area 값을 계산하거나 저장해 이후 처리에서 사용합니다.
            area = obj["area"]

            # 검출 영역을 알아보기 쉽도록 사각형을 그립니다.
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            # 중심점이나 원형 객체를 표시하기 위해 원을 그립니다.
            cv2.circle(
                frame,
                (center_x, center_y),
                5,
                (0, 0, 255),
                -1
            )

            # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
            cv2.putText(
                frame,
                f"Obj {index} Area {int(area)}",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (255, 0, 0),
                2
            )

        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("ROS2 Topic으로 보낼 객체 목록:", objects)

        # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
        cv2.imshow("ROS2 Ready Detection", frame)
        cv2.imshow("Mask", mask)

        # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료합니다.
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환합니다.
    cap.release()
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
