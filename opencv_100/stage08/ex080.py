"""예제 80. 로봇 비전에서 특징점 활용

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

# create_reference_features 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
def create_reference_features(reference_image):
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
    gray = cv2.cvtColor(reference_image, cv2.COLOR_BGR2GRAY)

    # 회전과 크기 변화에 비교적 강한 ORB 특징점 검출기를 만듭니다.
    orb = cv2.ORB_create(nfeatures=1000)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산합니다.
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료합니다.
    return orb, keypoints, descriptors

# match_with_reference 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
def match_with_reference(frame, orb, reference_descriptors):
    # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 이미지의 특징점 위치와 각 특징점을 설명하는 descriptor를 계산합니다.
    keypoints, descriptors = orb.detectAndCompute(gray, None)

    # result 변수에 이후 처리에 사용할 값을 저장합니다.
    result = {
        "detected": False,
        "good_match_count": 0,
        "total_match_count": 0
    }

    # 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
    if reference_descriptors is None or descriptors is None:
        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료합니다.
        return result

    # 두 이미지의 특징점 descriptor를 직접 비교하는 매처를 만듭니다.
    matcher = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

    # 두 이미지에서 서로 비슷한 특징점 쌍을 찾습니다.
    matches = matcher.match(reference_descriptors, descriptors)

    # good matches 변수에 이후 처리에 사용할 값을 저장합니다.
    good_matches = [
        match for match in matches
        if match.distance < 50
    ]

    # 검출되거나 매칭된 항목의 개수를 확인합니다.
    result["good_match_count"] = int(len(good_matches))
    result["total_match_count"] = int(len(matches))

    # 검출되거나 매칭된 항목의 개수를 확인합니다.
    if len(good_matches) > 30:
        result["detected"] = True

    # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료합니다.
    return result

# reference path 변수에 이후 처리에 사용할 값을 저장합니다.
reference_path = "practice_images/reference_object.jpg"

# 지정한 경로의 이미지 파일을 읽어 NumPy 배열로 저장합니다.
reference_image = cv2.imread(reference_path)

# 이미지나 검출 결과가 생성되지 않았는지 확인합니다.
if reference_image is None:
    # 현재 상태나 계산 결과를 터미널에 출력합니다.
    print("기준 이미지를 읽을 수 없습니다.")
# 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
else:
    orb, reference_keypoints, reference_descriptors = create_reference_features(
        reference_image
    )

    # 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 엽니다.
    cap = cv2.VideoCapture(0)

    # 카메라나 동영상 입력이 정상적으로 열렸는지 확인합니다.
    if not cap.isOpened():
        # 현재 상태나 계산 결과를 터미널에 출력합니다.
        print("카메라를 열 수 없습니다.")
    # 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
    else:
        # 조건이 참인 동안 아래 코드를 계속 반복합니다.
        while True:
            # 영상에서 프레임 한 장을 읽고, 성공 여부와 이미지 배열을 각각 받습니다.
            ret, frame = cap.read()

            # 필요한 조건이 충족되지 않았을 때의 처리를 시작합니다.
            if not ret:
                # 현재 상태나 계산 결과를 터미널에 출력합니다.
                print("프레임을 읽을 수 없습니다.")
                # 현재 반복문을 즉시 종료합니다.
                break

            # match result 변수에 이후 처리에 사용할 값을 저장합니다.
            match_result = match_with_reference(
                frame,
                orb,
                reference_descriptors
            )

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행합니다.
            if match_result["detected"]:
                # text 변수에 이후 처리에 사용할 값을 저장합니다.
                text = "Reference Object Detected"
                # color 변수에 이후 처리에 사용할 값을 저장합니다.
                color = (0, 255, 0)
            # 앞의 조건이 거짓인 경우 아래 코드를 실행합니다.
            else:
                # text 변수에 이후 처리에 사용할 값을 저장합니다.
                text = "Not Detected"
                # color 변수에 이후 처리에 사용할 값을 저장합니다.
                color = (0, 0, 255)

            # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
            cv2.putText(
                frame,
                text,
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                color,
                2
            )

            # 이미지 위에 상태나 좌표 정보를 글자로 표시합니다.
            cv2.putText(
                frame,
                f"Good Matches: {match_result['good_match_count']}",
                (20, 75),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0, 255, 255),
                2
            )

            # 현재 상태나 계산 결과를 터미널에 출력합니다.
            print("ROS2 Topic으로 보낼 매칭 결과:", match_result)

            # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
            cv2.imshow("Robot Vision Feature Matching", frame)

            # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
            if cv2.waitKey(1) == ord('q'):
                # 현재 반복문을 즉시 종료합니다.
                break

        # 카메라·동영상·VideoWriter 자원을 운영체제에 반환합니다.
        cap.release()
        # OpenCV가 만든 모든 이미지 창을 닫습니다.
        cv2.destroyAllWindows()
