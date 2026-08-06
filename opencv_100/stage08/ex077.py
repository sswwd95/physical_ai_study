"""예제 77. 이미지 유사도 비교

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

import cv2

def calculate_orb_similarity(image1, image2):
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create(nfeatures=1000)

    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    if descriptors1 is None or descriptors2 is None:
        return 0

    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    matches = matcher.match(descriptors1, descriptors2)

    good_matches = [
        match for match in matches if match.distance < 50
    ]

    return len(good_matches)

image1_path = "practice_images/object1.jpg"
image2_path = "practice_images/object2.jpg"

image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

if image1 is None or image2 is None:
    print("이미지를 읽을 수 없습니다.")
else:
    similarity_score = calculate_orb_similarity(image1, image2)

    print("ORB 유사도 점수:", similarity_score)

    if similarity_score > 30:
        print("두 이미지는 비슷한 물체일 가능성이 높습니다.")
    else:
        print("두 이미지는 다른 물체일 가능성이 높습니다.")
