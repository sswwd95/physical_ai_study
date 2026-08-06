"""예제 46. Bounding Box

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

# 사용할 입력 파일 또는 저장할 결과 파일의 경로를 문자열로 지정합니다.
image_path = "practice_images/sample.jpg"

# 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
image = cv2.imread(image_path)

# 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
if image is None:
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("이미지를 읽을 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용합니다.
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 기준값을 이용해 이미지를 흰색과 검은색의 이진 이미지로 나눕니다.
    ret, binary = cv2.threshold(
        blurred,
        127,
        255,
        cv2.THRESH_BINARY
    )

    # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
    contours, hierarchy = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 만듭니다.
    result = image.copy()
    # min area 값을 계산하거나 저장해 이후 처리에서 사용합니다.
    min_area = 500

    # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복합니다.
    for contour in contours:
        # 윤곽선이 차지하는 픽셀 면적을 계산합니다.
        area = cv2.contourArea(contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
        if area > min_area:
            # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산합니다.
            x, y, w, h = cv2.boundingRect(contour)

            # 검출 영역을 알아보기 쉽도록 사각형을 그립니다.
            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            # 현재 상태나 계산 결과를 터미널에 출력합니다.
            print("Bounding Box:", x, y, w, h)

    # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
    cv2.imshow("Bounding Box Result", result)

    # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
    cv2.waitKey(0)
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
