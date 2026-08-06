"""예제 78. Feature Matching 시각화

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

# image1 path 변수에 이후 처리에 사용할 값을 저장합니다.
image1_path = "practice_images/object1.jpg"
# image2 path 변수에 이후 처리에 사용할 값을 저장합니다.
image2_path = "practice_images/object2.jpg"

# 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
if image1 is None or image2 is None:
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("이미지를 읽을 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 회전과 크기 변화에 비교적 강한 ORB 특징점 검출기를 만듭니다.
    orb = cv2.ORB_create(nfeatures=1000)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산합니다.
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
    if descriptors1 is None or descriptors2 is None:
        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("특징점 descriptor가 부족합니다.")
    # 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
    else:
        # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 만듭니다.
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
        matches = matcher.match(descriptors1, descriptors2)

        # 결과를 비교하기 쉽도록 지정한 기준에 따라 정렬합니다.
        matches = sorted(matches, key=lambda x: x.distance)

        # good matches 변수에 이후 처리에 사용할 값을 저장합니다.
        good_matches = [
            match for match in matches
            if match.distance < 50
        ]

        # good matches 변수에 이후 처리에 사용할 값을 저장합니다.
        good_matches = good_matches[:50]

        # 두 이미지의 매칭된 특징점을 선으로 연결해 시각화합니다.
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

        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("좋은 매칭 개수:", len(good_matches))

        # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
        cv2.imshow("Feature Matching Visualization", match_image)

        # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
        cv2.waitKey(0)
        # OpenCV가 만든 모든 이미지 창을 닫습니다.
        cv2.destroyAllWindows()
