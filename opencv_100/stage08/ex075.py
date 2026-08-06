# ============================================================================
# 노션 원문 학습 설명: 예제 75. ORB 특징점 검출
# ============================================================================
#
# [핵심 주제]
# ORB는 이미지에서 특징적인 점을 찾아내는 알고리즘임
#
# 특징점은 코너, 모서리, 패턴이 뚜렷한 부분처럼 다른 위치와 구별되는 지점임
#
# ORB는 빠르고 무료로 사용할 수 있어 로봇 비전에서 많이 사용됨
#
# [실습 목표]
# 1. ORB 객체 생성
# 2. 특징점 검출
# 3. Descriptor 계산
# 4. 이미지 위에 특징점 그리기
#
# [실무에서 자주 하는 실수]
# 실수 1. 특징점이 없는 이미지에서 descriptors를 바로 사용
#
# 단색 벽이나 흐릿한 이미지에서는 특징점이 거의 없을 수 있음
#
# 이때 `descriptors`가 `None`일 수 있으므로 반드시 확인필요
#
# if descriptors is None:
# print("특징점 descriptor가 없습니다.")
#
# 실수 2. 특징점이 많을수록 무조건 좋다고 생각함
#
# 특징점이 너무 많으면 계산량이 증가함
#
# 실시간 로봇에서는 적절한 개수가 중요
#
# orb = cv2.ORB_create(nfeatures=500)
#
# 처음에는 500~1000 정도로 시작하는 것이 좋습니다.
#
# [ROS2와 연결되는 포인트]
# ORB 특징점은 다음 분야에 연결됨
#
# Visual SLAM
# Visual Odometry
# 이미지 매칭
# 마커 없는 물체 인식
# 장면 인식
#
# 로봇이 이동하면서 이전 프레임과 현재 프레임의 특징점을 비교하면 카메라 움직임을 추정할 수 있음
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/sample.jpg"

# 지정 경로의 이미지 읽기 및 NumPy 배열 저장
image = cv2.imread(image_path)

# 이미지 또는 검출 결과 생성 여부 확인
if image is None:
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("이미지를 읽을 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 회전과 크기 변화에 비교적 강한 ORB 특징점 검출기를 생성
    orb = cv2.ORB_create(nfeatures=500)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # result 변수에 이후 처리에 사용할 값을 저장
    result = cv2.drawKeypoints(
        image,
        keypoints,
        None,
        color=(0, 255, 0),
        flags=0
    )

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("검출된 특징점 개수:", len(keypoints))

    # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
    if descriptors is not None:
        # 현재 상태 또는 계산 결과의 터미널 출력
        print("Descriptor shape:", descriptors.shape)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("ORB Keypoints", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
