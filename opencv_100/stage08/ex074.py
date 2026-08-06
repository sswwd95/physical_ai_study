"""예제 74. Template Matching

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

scene_path = "practice_images/scene.jpg"
template_path = "practice_images/template.jpg"

scene = cv2.imread(scene_path)
template = cv2.imread(template_path)

if scene is None or template is None:
    print("이미지를 읽을 수 없습니다.")
else:
    scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)
    template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)

    result = cv2.matchTemplate(
        scene_gray,
        template_gray,
        cv2.TM_CCOEFF_NORMED
    )

    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    template_height, template_width = template_gray.shape[:2]

    top_left = max_loc
    bottom_right = (
        top_left[0] + template_width,
        top_left[1] + template_height
    )

    output = scene.copy()

    cv2.rectangle(
        output,
        top_left,
        bottom_right,
        (0, 0, 255),
        2
    )

    print("최고 유사도:", max_val)
    print("검출 위치:", top_left)

    cv2.imshow("Template", template)
    cv2.imshow("Matched Result", output)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
