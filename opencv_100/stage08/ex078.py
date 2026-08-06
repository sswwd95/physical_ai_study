# ============================================================================
# 노션 원문 학습 설명: 예제 78. Feature Matching 시각화
# ============================================================================
#
# [핵심 주제]
# Feature Matching 결과를 보기 좋게 시각화함
#
# 단순히 매칭 개수만 보는 것이 아니라, 실제로 어떤 점들이 연결되었는지 확인해야 잘못된 매칭을 찾을 수 있음
#
# [실습 목표]
# 1. ORB 특징점 매칭 복습
# 2. 좋은 매칭만 선별
# 3. cv2.drawMatches() 활용
# 4. 잘못된 매칭을 눈으로 확인
#
# [실무에서 자주 하는 실수]
# 실수 1. 매칭 선이 많으면 좋은 결과라고 착각
#
# 매칭 선이 많아도 잘못 연결된 선이 많으면 신뢰할 수 없음
#
# 시각화로 선이 자연스럽게 연결되는지 확인필요
#
# 실수 2. 모든 매칭을 다 그림
#
# 전체 매칭을 모두 그리면 화면이 복잡해지고 판단이 어렵습니다.
#
# 좋은 매칭 일부만 표시하는 것이 좋습니다.
#
# [ROS2와 연결되는 포인트]
# ROS2에서 특징점 기반 위치 추정이나 물체 인식을 디버깅할 때 매칭 시각화는 매우 중요
#
# 현재 프레임
# 기준 이미지
# → 특징점 매칭
# → 시각화 이미지 발행
# → rqt_image_view 또는 RViz2로 확인
#
# 알고리즘이 실패하는 이유를 눈으로 확인 가능
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# image1 path 변수에 이후 처리에 사용할 값을 저장
image1_path = "practice_images/object1.jpg"
# image2 path 변수에 이후 처리에 사용할 값을 저장
image2_path = "practice_images/object2.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
image1 = cv2.imread(image1_path)
image2 = cv2.imread(image2_path)

# 이미지 또는 검출 결과 생성 여부 확인
if image1 is None or image2 is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    gray1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

    # 회전과 크기 변화에 비교적 강한 ORB 특징점 검출기를 생성
    orb = cv2.ORB_create(nfeatures=1000)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산
    keypoints1, descriptors1 = orb.detectAndCompute(gray1, None)
    keypoints2, descriptors2 = orb.detectAndCompute(gray2, None)

    # 이미지 또는 검출 결과 생성 여부 확인
    if descriptors1 is None or descriptors2 is None:
        # 현재 상태 또는 계산 결과의 터미널 출력
        print("특징점 descriptor가 부족합니다.")
    # 앞 조건이 거짓일 때의 실행 구간
    else:
        # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 생성
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
        # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
        matches = matcher.match(descriptors1, descriptors2)

        # 결과를 비교하기 쉽도록 지정한 기준에 따라 정렬함
        matches = sorted(matches, key=lambda x: x.distance)

        # good matches 변수에 이후 처리에 사용할 값을 저장
        good_matches = [
            match for match in matches
            if match.distance < 50
        ]

        # good matches 변수에 이후 처리에 사용할 값을 저장
        good_matches = good_matches[:50]

        # 두 이미지의 매칭된 특징점을 선으로 연결해 시각화함
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

        # 현재 상태 또는 계산 결과의 터미널 출력
        print("좋은 매칭 개수:", len(good_matches))

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Feature Matching Visualization", match_image)

        # 키 입력 대기 및 실시간 영상 갱신
        cv2.waitKey(0)
        # 모든 OpenCV 이미지 창 닫기
        cv2.destroyAllWindows()
