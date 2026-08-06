# ============================================================================
# 노션 원문 학습 설명: 예제 79. 간단한 물체 인식
# ============================================================================
#
# [핵심 주제]
# 기준 이미지와 현재 이미지의 특징점 매칭을 이용해 물체가 있는지 판단함
#
# 이번 예제는 물체 인식의 매우 기초적인 형태임
#
# [실습 목표]
# 1. 기준 이미지와 장면 이미지 비교
# 2. ORB 매칭 기반 물체 존재 여부 판단
# 3. 좋은 매칭 개수 기준 적용
# 4. 인식 결과 표시
#
# [준비 파일]
# practice_images/reference_object.jpg
# practice_images/scene_with_object.jpg
#
# `reference_object.jpg`는 찾고 싶은 물체 이미지입니다.
#
# `scene_with_object.jpg`는 그 물체가 포함된 장면 이미지입니다.
#
# [실무에서 자주 하는 실수]
# 실수 1. 물체 위치까지 찾았다고 착각
#
# 이 예제는 물체가 있을 가능성을 판단하는 기초 예제임
#
# 정확한 물체 위치 영역을 찾으려면 Homography를 이용해 기준 이미지의 사각형을 장면 이미지에 투영필요
#
# 실수 2. 패턴이 없는 물체에 적용
#
# ORB 기반 인식은 다음 물체에 약함
#
# 단색 공
# 반짝이는 금속
# 투명 물체
# 무늬 없는 박스
# 흐릿한 이미지
#
# 이런 경우 색상 검출, 모양 검출, 딥러닝 검출을 고려필요
#
# [ROS2와 연결되는 포인트]
# ROS2에서 기준 물체 인식 노드를 만들 때 사용 가능
#
# 기준 이미지 로드
# /camera/image_raw 수신
# 현재 프레임과 ORB 매칭
# 매칭 개수 기준으로 물체 존재 판단
# /object_detected Topic 발행
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# reference path 변수에 이후 처리에 사용할 값을 저장
reference_path = "practice_images/reference_object.jpg"
# scene path 변수에 이후 처리에 사용할 값을 저장
scene_path = "practice_images/scene_with_object.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
reference = cv2.imread(reference_path)
scene = cv2.imread(scene_path)

# 이미지 또는 검출 결과 생성 여부 확인
if reference is None or scene is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    ref_gray = cv2.cvtColor(reference, cv2.COLOR_BGR2GRAY)
    scene_gray = cv2.cvtColor(scene, cv2.COLOR_BGR2GRAY)

    # 회전과 크기 변화에 비교적 강한 ORB 특징점 검출기를 생성
    orb = cv2.ORB_create(nfeatures=1500)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산
    ref_keypoints, ref_descriptors = orb.detectAndCompute(ref_gray, None)
    scene_keypoints, scene_descriptors = orb.detectAndCompute(scene_gray, None)

    # 이미지 또는 검출 결과 생성 여부 확인
    if ref_descriptors is None or scene_descriptors is None:
        # 현재 상태 또는 계산 결과의 터미널 출력
        print("특징점 descriptor가 부족합니다.")
    # 앞 조건이 거짓일 때의 실행 구간
    else:
        # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 생성
        matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

        # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
        matches = matcher.match(ref_descriptors, scene_descriptors)

        # good matches 변수에 이후 처리에 사용할 값을 저장
        good_matches = [
            match for match in matches
            if match.distance < 50
        ]

        # 현재 상태 또는 계산 결과의 터미널 출력
        print("좋은 매칭 개수:", len(good_matches))

        # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 생성
        output = scene.copy()

        # 검출되거나 매칭된 항목의 개수를 확인
        if len(good_matches) > 30:
            # result text 변수에 이후 처리에 사용할 값을 저장
            result_text = "Object Detected"
            # color 변수에 이후 처리에 사용할 값을 저장
            color = (0, 255, 0)
        # 앞 조건이 거짓일 때의 실행 구간
        else:
            # result text 변수에 이후 처리에 사용할 값을 저장
            result_text = "Object Not Detected"
            # color 변수에 이후 처리에 사용할 값을 저장
            color = (0, 0, 255)

        # 이미지 위에 상태나 좌표 정보를 글자로 표시
        cv2.putText(
            output,
            result_text,
            (30, 50),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            color,
            2
        )

        # 두 이미지의 매칭된 특징점을 선으로 연결해 시각화함
        match_view = cv2.drawMatches(
            reference,
            ref_keypoints,
            scene,
            scene_keypoints,
            sorted(good_matches, key=lambda x: x.distance)[:50],
            None,
            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS
        )

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Recognition Result", output)
        cv2.imshow("Matching View", match_view)

        # 키 입력 대기 및 실시간 영상 갱신
        cv2.waitKey(0)
        # 모든 OpenCV 이미지 창 닫기
        cv2.destroyAllWindows()
