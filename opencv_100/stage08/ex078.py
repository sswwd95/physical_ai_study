"""예제 78. Feature Matching 시각화

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

image1_path = "practice_images/object1.jpg"
image2_path = "practice_images/object2.jpg"

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

if image1 is None or image2 is None:
    print("이미지를 읽을 수 없습니다.")
else:
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=1000)

    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    if descriptors1 is None or descriptors2 is None:
        print("특징점 descriptor가 부족합니다.")
    else:
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        matches = matcher.match(descriptors1, descriptors2)

        matches = sorted(matches, key=lambda x: x.distance)

        good_matches = [
            match for match in matches
            if match.distance < 50
        ]

        good_matches = good_matches[:50]

        match_image = cv2.drawMatches(
            image1,
            keypoints1,
            image2,
            keypoints2,
            good_matches,
            None,
            matchColor=(0, 255, 0),
            singlePointColor=(255, 0, 0),
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
        )

        print("좋은 매칭 개수:", len(good_matches))

        cv2.imshow("Feature Matching Visualization", match_image)

        cv2.waitKey(0)
        cv2.destroyAllWindows()
