"""예제 79. 간단한 물체 인식

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

reference_path = "practice_images/reference_object.jpg"
scene_path = "practice_images/scene_with_object.jpg"

reference = cv2.imread(reference_path)
scene = cv2.imread(scene_path)

if reference is None or scene is None:
    print("이미지를 읽을 수 없습니다.")
else:
    ref_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=1500)

    ref_keypoints, ref_descriptors = orb.detectAndCompute(ref_gray, None)
    scene_keypoints, scene_descriptors = orb.detectAndCompute(scene_gray, None)

    if ref_descriptors is None or scene_descriptors is None:
        print("특징점 descriptor가 부족합니다.")
    else:
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        matches = matcher.match(ref_descriptors, scene_descriptors)

        good_matches = [
            match for match in matches
            if match.distance < 50
        ]

        print("좋은 매칭 개수:", len(good_matches))

        output = scene.copy()

        if len(good_matches) > 30:
            result_text = "Object Detected"
            color = (0, 255, 0)
        else:
            result_text = "Object Not Detected"
            color = (0, 0, 255)

        cv2.putText(
            output,
            result_text,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            color,
            2
        )

        match_view = cv2.drawMatches(
            reference,
            ref_keypoints,
            scene,
            scene_keypoints,
            sorted(good_matches, key=lambda x: x.distance)[:50],
            None,
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
        )

        cv2.imshow("Recognition Result", output)
        cv2.imshow("Matching View", match_view)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
