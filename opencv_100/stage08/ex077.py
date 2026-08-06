"""예제 77. 이미지 유사도 비교

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

# calculate_orb_similarity 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
def calculate_orb_similarity(image1, image2):
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
        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료합니다.
        return 0

    # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 만듭니다.
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
    matches = matcher.match(descriptors1, descriptors2)

    # good matches 변수에 이후 처리에 사용할 값을 저장합니다.
    good_matches = [
        match for match in matches if match.distance < 50
    ]

    # 검출되거나 매칭된 항목의 개수를 확인합니다.
    return len(good_matches)

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
    # similarity score 변수에 이후 처리에 사용할 값을 저장합니다.
    similarity_score = calculate_orb_similarity(image1, image2)

    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("ORB 유사도 점수:", similarity_score)

    # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
    if similarity_score > 30:
        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("두 이미지는 비슷한 물체일 가능성이 높습니다.")
    # 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
    else:
        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("두 이미지는 다른 물체일 가능성이 높습니다.")
