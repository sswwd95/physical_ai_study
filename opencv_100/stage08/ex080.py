"""예제 80. 로봇 비전에서 특징점 활용

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

def create_reference_features(reference_image):
    gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=1000)

    keypoints, descriptors = orb.detectAndCompute(gray, None)

    return orb, keypoints, descriptors

def match_with_reference(frame, orb, reference_descriptors):
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    keypoints, descriptors = orb.detectAndCompute(gray, None)

    result = {
        "detected": False,
        "good_match_count": 0,
        "total_match_count": 0
    }

    if reference_descriptors is None or descriptors is None:
        return result

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = matcher.match(reference_descriptors, descriptors)

    good_matches = [
        match for match in matches
        if match.distance < 50
    ]

    result["good_match_count"] = int(len(good_matches))
    result["total_match_count"] = int(len(matches))

    if len(good_matches) > 30:
        result["detected"] = True

    return result

reference_path = "practice_images/reference_object.jpg"

reference_image = cv2.imread(reference_path)

if reference_image is None:
    print("기준 이미지를 읽을 수 없습니다.")
else:
    orb, reference_keypoints, reference_descriptors = create_reference_features(
        reference_image
    )

    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("카메라를 열 수 없습니다.")
    else:
        while True:
            ret, frame = cap.read()

            if not ret:
                print("프레임을 읽을 수 없습니다.")
                break

            match_result = match_with_reference(
                frame,
                orb,
                reference_descriptors
            )

            if match_result["detected"]:
                text = "Reference Object Detected"
                color = (0, 255, 0)
            else:
                text = "Not Detected"
                color = (0, 0, 255)

            cv2.putText(
                frame,
                text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            cv2.putText(
                frame,
                f"Good Matches: {match_result['good_match_count']}",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            print("ROS2 Topic으로 보낼 매칭 결과:", match_result)

            cv2.imshow("Robot Vision Feature Matching", frame)

            if cv2.waitKey(1) == ord('q'):
                break

        cap.release()
        cv2.destroyAllWindows()
