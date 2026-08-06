"""예제 41. Sobel Edge

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

    # 가로 또는 세로 방향의 밝기 변화량을 계산해 경계선을 찾습니다.
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # 픽셀값이 0~255 범위를 벗어나지 않도록 안전하게 밝기·대비를 조절합니다.
    sobel_x_abs = cv2.convertScaleAbs(sobel_x)
    sobel_y_abs = cv2.convertScaleAbs(sobel_y)

    # sobel combined 변수에 이후 처리에 사용할 값을 저장합니다.
    sobel_combined = cv2.addWeighted(
        sobel_x_abs,
        0.5,
        sobel_y_abs,
        0.5,
        0
    )

    # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
    cv2.imshow("Gray Image", gray)
    cv2.imshow("Sobel X", sobel_x_abs)
    cv2.imshow("Sobel Y", sobel_y_abs)
    cv2.imshow("Sobel Combined", sobel_combined)

    # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
    cv2.waitKey(0)
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
