"""예제 4. 이미지 저장

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
save_path = "practice_images/output_sample.jpg"

# 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
image = cv2.imread(image_path)

# 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
if image is None:
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("이미지를 읽을 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    # 현재 이미지 배열을 지정한 경로의 이미지 파일로 저장합니다.
    result = cv2.imwrite(save_path, image)

    # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
    if result:
        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("이미지 저장 성공:", save_path)
    # 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
    else:
        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("이미지 저장 실패")
