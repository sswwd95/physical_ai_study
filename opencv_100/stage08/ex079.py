"""예제 79. 간단한 물체 인식

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

# reference path 변수에 이후 처리에 사용할 값을 저장합니다.
reference_path = "practice_images/reference_object.jpg"
# scene path 변수에 이후 처리에 사용할 값을 저장합니다.
scene_path = "practice_images/scene_with_object.jpg"

# 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
reference = cv2.imread(reference_path)
scene = cv2.imread(scene_path)

# 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
if reference is None or scene is None:
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("이미지를 읽을 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
    ref_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)

    # 회전과 크기 변화에 비교적 강한 ORB 특징점 검출기를 만듭니다.
    orb = cv2.ORB_create(nfeatures=1500)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산합니다.
    ref_keypoints, ref_descriptors = orb.detectAndCompute(ref_gray, None)
    scene_keypoints, scene_descriptors = orb.detectAndCompute(scene_gray, None)

    # 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
    if ref_descriptors is None or scene_descriptors is None:
        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("특징점 descriptor가 부족합니다.")
    # 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
    else:
        # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 만듭니다.
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
        matches = matcher.match(ref_descriptors, scene_descriptors)

        # good matches 변수에 이후 처리에 사용할 값을 저장합니다.
        good_matches = [
            match for match in matches
            if match.distance < 50
        ]

        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("좋은 매칭 개수:", len(good_matches))

        # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 만듭니다.
        output = scene.copy()

        # 검출되거나 매칭된 항목의 개수를 확인합니다.
        if len(good_matches) > 30:
            # result text 변수에 이후 처리에 사용할 값을 저장합니다.
            result_text = "Object Detected"
            # color 변수에 이후 처리에 사용할 값을 저장합니다.
            color = (0, 255, 0)
        # 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
        else:
            # result text 변수에 이후 처리에 사용할 값을 저장합니다.
            result_text = "Object Not Detected"
            # color 변수에 이후 처리에 사용할 값을 저장합니다.
            color = (0, 0, 255)

        # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
        cv2.putText(
            output,
            result_text,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            color,
            2
        )

        # 두 이미지의 매칭된 특징점을 선으로 연결해 시각화합니다.
        match_view = cv2.drawMatches(
            reference,
            ref_keypoints,
            scene,
            scene_keypoints,
            sorted(good_matches, key=lambda x: x.distance)[:50],
            None,
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
        )

        # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
        cv2.imshow("Recognition Result", output)
        cv2.imshow("Matching View", match_view)

        # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
        cv2.waitKey(0)
        # OpenCV가 만든 모든 이미지 창을 닫습니다.
        cv2.destroyAllWindows()
