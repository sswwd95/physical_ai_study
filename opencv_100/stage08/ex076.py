# ============================================================================
# 노션 원문 학습 설명: 예제 76. ORB 특징점 매칭
# ============================================================================
#
# [핵심 주제]
# 두 이미지에서 ORB 특징점을 검출하고, 서로 비슷한 특징점을 매칭함
#
# 이미지 매칭은 같은 물체나 같은 장소인지 판단하는 데 사용 가능
#
# [실습 목표]
# 1. 두 이미지에서 ORB 특징점 검출
# 2. Descriptor 매칭
# 3. BFMatcher 사용법 이해
# 4. 매칭 결과 시각화
#
# [준비 파일]
# practice_images/object1.jpg
# practice_images/object2.jpg
#
# 두 이미지는 같은 물체를 다른 각도 또는 거리에서 촬영한 이미지가 좋습니다.
#
# [실무에서 자주 하는 실수]
# 실수 1. ORB descriptor에 L2 거리 사용
#
# SIFT 같은 실수형 descriptor는 L2를 쓰지만, ORB는 이진 descriptor이므로 Hamming 거리를 사용필요
#
# cv2.NORM_HAMMING
#
# 실수 2. 매칭 개수만 보고 같은 물체라고 판단
#
# 매칭 개수가 많다고 반드시 같은 물체는 아님
#
# 잘못된 매칭도 포함될 수 있음
#
# 실무에서는 거리 기준, RANSAC, Homography 검증 등을 추가
#
# [ROS2와 연결되는 포인트]
# ORB 매칭은 다음 작업에 사용 가능
#
# 로봇이 이전에 본 장소인지 판단
# 특정 패턴 물체 재인식
# 카메라 이동량 추정
# Visual SLAM 특징점 매칭
#
# ROS2에서 카메라 프레임 간 특징점을 매칭하면 로봇의 시각적 움직임 추정으로 확장할 수 있음
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
        matcher = cv2.BFMatcher(
            cv2.NORM_HAMMING,
            crossCheck=True
        )

        # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
        matches = matcher.match(descriptors1, descriptors2)

        # 결과를 비교하기 쉽도록 지정한 기준에 따라 정렬함
        matches = sorted(matches, key=lambda x: x.distance)

        # good matches 변수에 이후 처리에 사용할 값을 저장
        good_matches = matches[:50]

        # 두 이미지의 매칭된 특징점을 선으로 연결해 시각화함
        result = cv2.drawMatches(
            image1,
            keypoints1,
            image2,
            keypoints2,
            good_matches,
            None,
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
        )

        # 현재 상태 또는 계산 결과의 터미널 출력
        print("전체 매칭 개수:", len(matches))
        print("표시한 좋은 매칭 개수:", len(good_matches))

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("ORB Matching", result)

        # 키 입력 대기 및 실시간 영상 갱신
        cv2.waitKey(0)
        # 모든 OpenCV 이미지 창 닫기
        cv2.destroyAllWindows()
