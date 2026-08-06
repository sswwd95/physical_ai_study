"""예제 98. 로봇 팔 Pick 위치 계산

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

# 사용할 입력 파일 또는 저장할 결과 파일의 경로를 문자열로 지정합니다.
image_path = "practice_images/workpiece.jpg"

# 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
image = cv2.imread(image_path)

# 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
if image is None:
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("이미지를 읽을 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    height, width = image.shape[:2]

    # workspace width mm 값을 계산하거나 저장해 이후 처리에서 사용합니다.
    workspace_width_mm = 400
    # workspace height mm 값을 계산하거나 저장해 이후 처리에서 사용합니다.
    workspace_height_mm = 300

    # 색상 검출이 쉬운 HSV 색상 공간으로 변환합니다.
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 여러 숫자를 NumPy 배열로 묶어 좌표나 색상 범위를 표현합니다.
    lower_object = np.array([20, 80, 80])
    upper_object = np.array([40, 255, 255])

    # 지정한 최솟값과 최댓값 사이에 있는 픽셀만 흰색으로 만든 마스크를 생성합니다.
    mask = cv2.inRange(hsv, lower_object, upper_object)

    # 형태학적 연산이나 필터에 사용할 값이 1인 커널 배열을 만듭니다.
    kernel = np.ones((5, 5), np.uint8)
    # 작은 흰색 노이즈를 제거하기 위해 열기 연산을 적용합니다.
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    # 객체 내부의 작은 검은 구멍을 메우기 위해 닫기 연산을 적용합니다.
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)

    # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
    contours, _ = cv2.findContours(
        mask,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 만듭니다.
    result = image.copy()

    # 검출되거나 매칭된 항목의 개수를 확인합니다.
    if len(contours) > 0:
        # 윤곽선이 차지하는 픽셀 면적을 계산합니다.
        largest_contour = max(contours, key=cv2.contourArea)
        area = cv2.contourArea(largest_contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
        if area > 500:
            # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산합니다.
            x, y, w, h = cv2.boundingRect(largest_contour)

            # center x 값을 계산하거나 저장해 이후 처리에서 사용합니다.
            center_x = x + w // 2
            # center y 값을 계산하거나 저장해 이후 처리에서 사용합니다.
            center_y = y + h // 2

            # robot x mm 변수에 이후 처리에 사용할 값을 저장합니다.
            robot_x_mm = center_x / width * workspace_width_mm
            # robot y mm 변수에 이후 처리에 사용할 값을 저장합니다.
            robot_y_mm = center_y / height * workspace_height_mm

            # 검출 영역을 알아보기 쉽도록 사각형을 그립니다.
            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (0, 255, 0),
                2
            )

            # 중심점이나 원형 객체를 표시하기 위해 원을 그립니다.
            cv2.circle(
                result,
                (center_x, center_y),
                6,
                (0, 0, 255),
                -1
            )

            # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
            cv2.putText(
                result,
                f"Pick mm: ({robot_x_mm:.1f}, {robot_y_mm:.1f})",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            # 현재 상태나 계산 결과를 터미널에 출력합니다.
            print("픽셀 좌표:", center_x, center_y)
            print("로봇 Pick 좌표 근사 mm:", robot_x_mm, robot_y_mm)

    # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
    cv2.imshow("Pick Position", result)
    cv2.imshow("Mask", mask)

    # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
    cv2.waitKey(0)
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
