# ============================================================================
# 노션 원문 학습 설명: 예제 77. 이미지 유사도 비교
# ============================================================================
#
# [핵심 주제]
# 두 이미지가 얼마나 비슷한지 ORB 특징점 매칭 개수를 기준으로 간단히 판단함
#
# 완벽한 유사도 알고리즘은 아니지만, 초보자가 이미지 매칭 개념을 이해하기에 좋습니다.
#
# [실습 목표]
# 1. ORB 매칭 기반 유사도 개념 이해
# 2. 좋은 매칭 개수 계산
# 3. 임계값으로 유사/비유사 판단
# 4. 간단한 물체 인식 기초 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. threshold 값을 모든 이미지에 동일하게 사용
#
# if similarity_score > 30:
#
# 이 값은 실습용 기준임
#
# 이미지 크기, 특징점 수, 물체 패턴에 따라 적절한 기준은 변화
#
# 실수 2. 단색 물체에 ORB 유사도를 적용
#
# ORB는 코너나 패턴이 많은 이미지에서 잘 작동함
#
# 단색 공, 단색 박스처럼 특징점이 적은 물체에는 적합하지 않을 수 있음
#
# 이런 경우 색상 기반 검출이나 딥러닝 검출이 더 낫습니다.
#
# [ROS2와 연결되는 포인트]
# 로봇이 현재 보고 있는 물체가 기준 이미지와 같은지 판단할 때 사용 가능
#
# 기준 부품 이미지
# 현재 카메라 프레임의 ROI
# → ORB 유사도 비교
# → 같은 부품인지 판단
#
# 단, 실제 프로젝트에서는 조명과 회전, 스케일 변화에 대한 검증이 추가로 필요
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# calculate_orb_similarity 작업을 반복해서 사용할 수 있도록 함수로 정의함
def calculate_orb_similarity(image1, image2):
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
        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
        return 0

    # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 생성
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
    matches = matcher.match(descriptors1, descriptors2)

    # good matches 변수에 이후 처리에 사용할 값을 저장
    good_matches = [
        match for match in matches if match.distance < 50
    ]

    # 검출되거나 매칭된 항목의 개수를 확인
    return len(good_matches)

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
    # similarity score 변수에 이후 처리에 사용할 값을 저장
    similarity_score = calculate_orb_similarity(image1, image2)

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("ORB 유사도 점수:", similarity_score)

    # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
    if similarity_score > 30:
        # 현재 상태 또는 계산 결과의 터미널 출력
        print("두 이미지는 비슷한 물체일 가능성이 높습니다.")
    # 앞 조건이 거짓일 때의 실행 구간
    else:
        # 현재 상태 또는 계산 결과의 터미널 출력
        print("두 이미지는 다른 물체일 가능성이 높습니다.")
