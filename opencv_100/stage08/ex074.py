"""예제 74. Template Matching

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

# scene path 변수에 이후 처리에 사용할 값을 저장합니다.
scene_path = "practice_images/scene.jpg"
# template path 변수에 이후 처리에 사용할 값을 저장합니다.
template_path = "practice_images/template.jpg"

# 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
scene = cv2.imread(scene_path)
template = cv2.imread(template_path)

# 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
if scene is None or template is None:
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("이미지를 읽을 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
    scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    # 작은 템플릿 이미지가 원본의 어느 위치와 가장 비슷한지 계산합니다.
    result = cv2.matchTemplate(
        scene_gray,
        template_gray,
        cv2.TM_CCOEFF_NORMED
    )

    # 행렬에서 최솟값·최댓값과 해당 위치를 찾습니다.
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    template_height, template_width = template_gray.shape[:2]

    # top left 변수에 이후 처리에 사용할 값을 저장합니다.
    top_left = max_loc
    # bottom right 변수에 이후 처리에 사용할 값을 저장합니다.
    bottom_right = (
        top_left[0] + template_width,
        top_left[1] + template_height
    )

    # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 만듭니다.
    output = scene.copy()

    # 검출 영역을 알아보기 쉽도록 사각형을 그립니다.
    cv2.rectangle(
        output,
        top_left,
        bottom_right,
        (0, 0, 255),
        2
    )

    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("최고 유사도:", max_val)
    print("검출 위치:", top_left)

    # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
    cv2.imshow("Template", template)
    cv2.imshow("Matched Result", output)

    # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
    cv2.waitKey(0)
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
