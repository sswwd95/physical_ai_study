# ============================================================================
# 노션 원문 학습 설명: 예제 80. 로봇 비전에서 특징점 활용
# ============================================================================
#
# [핵심 주제]
# 특징점 매칭 결과를 로봇 비전 관점에서 사용할 수 있도록 구조화함
#
# 이번 예제에서는 카메라 프레임에서 기준 이미지와 매칭되는 정도를 계산하고, 결과를 딕셔너리로 정리함
#
# ROS2 Topic으로 발행하기 좋은 형태임
#
# [실습 목표]
# 1. 기준 이미지 특징점 미리 계산
# 2. 현재 프레임 특징점 계산
# 3. 좋은 매칭 개수 계산
# 4. ROS2 메시지 변환 준비
#
# [실무에서 자주 하는 실수]
# 실수 1. 기준 이미지 특징점을 매 프레임 계산
#
# 기준 이미지는 변하지 않으므로 한 번만 계산필요
#
# 나쁜 구조:
#
# 매 프레임마다 기준 이미지 로드
# 매 프레임마다 기준 이미지 ORB 계산
#
# 좋은 구조:
#
# 시작 시 기준 이미지 ORB 계산
# 매 프레임에서는 현재 프레임만 ORB 계산
#
# 실수 2. detected만 발행하고 신뢰도 정보를 보내지 않음
#
# 실무에서는 True/False만 보내면 디버깅이 어렵습니다.
#
# 다음 정보를 함께 보내는 것이 좋습니다.
#
# detected
# good_match_count
# total_match_count
# threshold
# timestamp
#
# [ROS2와 연결되는 포인트]
# 이 예제의 결과 구조는 ROS2 메시지로 바꾸기 쉽습니다.
#
# {
# "detected": true,
# "good_match_count": 42,
# "total_match_count": 128
# }
#
# 간단한 실습에서는 `std_msgs/String`으로 JSON 문자열을 발행할 수 있고, 정식 프로젝트에서는 커스텀 메시지를 만드는 것이 좋습니다.
#
# 예상 ROS2 흐름은 다음과 같습니다.
#
# reference_object.jpg 로드
# → 기준 특징점 계산
# → /camera/image_raw Subscribe
# → 현재 프레임 특징점 계산
# → 기준 특징점과 매칭
# → detected, good_match_count 발행
#
# # 8단계 핵심 정리
#
# 이번 8단계에서는 색상 기반 검출을 넘어 패턴, 특징점, 이미지 유사도를 다루었습니다.
#
# | 예제 | 핵심 내용 |
# | --- | --- |
# | 71 | 이미지 히스토그램 |
# | 72 | 히스토그램 평활화 |
# | 73 | CLAHE |
# | 74 | Template Matching |
# | 75 | ORB 특징점 검출 |
# | 76 | ORB 특징점 매칭 |
# | 77 | 이미지 유사도 비교 |
# | 78 | Feature Matching 시각화 |
# | 79 | 간단한 물체 인식 |
# | 80 | 로봇 비전에서 특징점 활용 |
#
# # 초보자가 반드시 기억해야 할 핵심 문법
#
# hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
#
# 이미지 밝기 히스토그램을 계산
#
# equalized = cv2.equalizeHist(gray)
#
# 흑백 이미지의 대비를 개선함
#
# clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8, 8))
# clahe_image = clahe.apply(gray)
#
# CLAHE로 부분 대비를 개선함
#
# result = cv2.matchTemplate(scene_gray, template_gray, cv2.TM_CCOEFF_NORMED)
# min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
#
# 템플릿 매칭으로 가장 유사한 위치를 찾습니다.
#
# orb = cv2.ORB_create(nfeatures=1000)
# keypoints, descriptors = orb.detectAndCompute(gray, None)
#
# ORB 특징점과 descriptor를 계산
#
# matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
# matches = matcher.match(descriptors1, descriptors2)
#
# ORB descriptor를 매칭함
#
# matches = sorted(matches, key=lambda x: x.distance)
#
# 좋은 매칭 순서로 정렬함
#
# match_image = cv2.drawMatches(
# image1,
# keypoints1,
# image2,
# keypoints2,
# good_matches,
# None
# )
#
# 특징점 매칭 결과를 시각화함
#
# # ROS2 Humble 강의 전 관점에서 중요한 이유
#
# 이번 단계는 ROS2 로봇 비전에서 다음 주제와 연결됨
#
# Visual SLAM
# Visual Odometry
# 마커 없는 물체 인식
# 기준 이미지 기반 물체 탐색
# 작업대 부품 인식
# 장면 유사도 판단
#
# 색상 기반 검출이 다음에 적합하다면,
#
# 빨간 공
# 파란 표식
# 초록 라인
# 색상이 뚜렷한 물체
#
# 특징점 기반 검출은 다음에 적합
#
# 로고가 있는 물체
# 무늬가 있는 부품
# 패턴이 있는 마커
# 책 표지
# 기계 부품의 텍스처
#
# # 실무 기준 선택표
#
# | 상황 | 추천 방법 |
# | --- | --- |
# | 밝기 상태를 분석하고 싶음 | 히스토그램 |
# | 대비가 낮음 | Histogram Equalization |
# | 조명이 고르지 않음 | CLAHE |
# | 동일 크기 패턴을 찾고 싶음 | Template Matching |
# | 회전/시점 변화가 조금 있음 | ORB 특징점 |
# | 두 이미지가 같은 물체인지 비교 | ORB Matching |
# | 매칭 오류를 확인하고 싶음 | drawMatches 시각화 |
# | ROS2 Topic으로 인식 결과 발행 | 결과 dict 구조화 |
#
# # 실무에서 가장 중요한 판단 기준
#
# 색상이 뚜렷하면 HSV 기반 검출이 빠르고 쉽다.
# 패턴이 뚜렷하면 ORB 특징점 매칭이 유용하다.
# 템플릿 매칭은 크기와 회전 변화에 약하다.
# ORB는 단색 물체에 약하다.
# 조명 문제가 있으면 CLAHE나 평활화를 고려한다.
# 실시간 ROS2에서는 계산량과 FPS를 반드시 확인한다.
#
# - 9단계: ROS2 연계를 위한 실전 OpenCV
#
# 이번 단계는 지금까지 배운 OpenCV 문법을 ROS2 Humble 카메라 노드 구조로 연결하는 핵심 구간임
#
# OpenCV 단독 실습에서는 보통 이렇게 처리했습니다.
#
# cv2.VideoCapture()
# → frame 읽기
# → OpenCV 처리
# → cv2.imshow()
#
# ROS2에서는 구조가 다음처럼 변경
#
# /camera/image_raw Subscribe
# → cv_bridge로 ROS2 Image 메시지를 OpenCV frame으로 변환
# → OpenCV 처리
# → 결과 이미지 또는 좌표 Topic Publish
#
# # 9단계: ROS2 연계를 위한 실전 OpenCV
#
# | 번호 | 핵심 주제 |
# | --- | --- |
# | 81 | cv_bridge 개념 |
# | 82 | ROS2 Image 메시지 이해 |
# | 83 | OpenCV 이미지를 ROS2 메시지로 변환 |
# | 84 | ROS2 Image 메시지를 OpenCV로 변환 |
# | 85 | 카메라 노드 구조 설계 |
# | 86 | 이미지 Subscriber 구조 |
# | 87 | 실시간 Edge Publisher |
# | 88 | 객체 중심 좌표 Publisher |
# | 89 | 로봇 추종용 비전 노드 |
# | 90 | OpenCV + ROS2 디버깅 포인트 |
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# create_reference_features 작업을 반복해서 사용할 수 있도록 함수로 정의함
def create_reference_features(reference_image):
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    # 회전과 크기 변화에 비교적 강한 ORB 특징점 검출기를 생성
    orb = cv2.ORB_create(nfeatures=1000)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
    return orb, keypoints, descriptors

# match_with_reference 작업을 반복해서 사용할 수 있도록 함수로 정의함
def match_with_reference(frame, orb, reference_descriptors):
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # result 변수에 이후 처리에 사용할 값을 저장
    result = {
        "detected": False,
        "good_match_count": 0,
        "total_match_count": 0
    }

    # 이미지 또는 검출 결과 생성 여부 확인
    if reference_descriptors is None or descriptors is None:
        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
        return result

    # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 생성
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
    matches = matcher.match(reference_descriptors, descriptors)

    # good matches 변수에 이후 처리에 사용할 값을 저장
    good_matches = [
        match for match in matches
        if match.distance < 50
    ]

    # 검출되거나 매칭된 항목의 개수를 확인
    result["good_match_count"] = int(len(good_matches))
    result["total_match_count"] = int(len(matches))

    # 검출되거나 매칭된 항목의 개수를 확인
    if len(good_matches) > 30:
        result["detected"] = True

    # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
    return result

# reference path 변수에 이후 처리에 사용할 값을 저장
reference_path = "practice_images/reference_object.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
reference_image = cv2.imread(reference_path)

# 이미지 또는 검출 결과 생성 여부 확인
if reference_image is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("기준 이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    orb, reference_keypoints, reference_descriptors = create_reference_features(
        reference_image
    )

    # 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 열기
    cap = cv2.VideoCapture(0)

    # 카메라나 동영상 입력이 정상적으로 열렸는지 확인
    if not cap.isOpened():
        # 현재 상태 또는 계산 결과의 터미널 출력
        print("카메라를 열 수 없습니다.")
    # 앞 조건이 거짓일 때의 실행 구간
    else:
        # 조건이 참인 동안 아래 코드를 계속 반복
        while True:
            # 영상에서 프레임 한 장을 읽고, 성공 여부와 이미지 배열을 각각 수신
            ret, frame = cap.read()

            # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
            if not ret:
                # 현재 상태 또는 계산 결과의 터미널 출력
                print("프레임을 읽을 수 없습니다.")
                # 현재 반복문을 즉시 종료
                break

            # match result 변수에 이후 처리에 사용할 값을 저장
            match_result = match_with_reference(
                frame,
                orb,
                reference_descriptors
            )

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
            if match_result["detected"]:
                # text 변수에 이후 처리에 사용할 값을 저장
                text = "Reference Object Detected"
                # color 변수에 이후 처리에 사용할 값을 저장
                color = (0, 255, 0)
            # 앞 조건이 거짓일 때의 실행 구간
            else:
                # text 변수에 이후 처리에 사용할 값을 저장
                text = "Not Detected"
                # color 변수에 이후 처리에 사용할 값을 저장
                color = (0, 0, 255)

            # 이미지 위에 상태나 좌표 정보를 글자로 표시
            cv2.putText(
                frame,
                text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # 이미지 위에 상태나 좌표 정보를 글자로 표시
            cv2.putText(
                frame,
                f"Good Matches: {match_result['good_match_count']}",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            # 현재 상태 또는 계산 결과의 터미널 출력
            print("ROS2 Topic으로 보낼 매칭 결과:", match_result)

            # 처리 결과 확인용 OpenCV 창 표시
            cv2.imshow("Robot Vision Feature Matching", frame)

            # 키 입력 대기 및 실시간 영상 갱신
            if cv2.waitKey(1) == ord('q'):
                # 현재 반복문을 즉시 종료
                break

        # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
        cap.release()
        # 모든 OpenCV 이미지 창 닫기
        cv2.destroyAllWindows()
