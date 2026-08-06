# ============================================================================
# 노션 원문 학습 설명: 예제 47. 최소 외접 원
# ============================================================================
#
# [핵심 주제]
# 최소 외접 원은 Contour를 포함하는 가장 작은 원임
#
# 공, 원형 마커, 둥근 부품을 검출할 때 유용
#
# [실습 목표]
# 1. cv2.minEnclosingCircle() 사용법 이해
# 2. 객체 중심 좌표 계산
# 3. 반지름 계산
# 4. 원형 객체 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. 모든 객체에 원을 적용
#
# 최소 외접 원은 원형 객체에 특히 적합
#
# 사각형이나 길쭉한 물체에 적용하면 실제 모양과 맞지 않을 수 있음
#
# 실수 2. 반지름이 작은 객체를 노이즈로 제거하지 않음
#
# 작은 점도 원으로 검출될 수 있음
#
# 면적 또는 반지름 기준으로 필터링하는 것이 좋습니다.
#
# ifradius>10:
# # 의미 있는 원형 객체로 처리
#
# [ROS2와 연결되는 포인트]
# 공 추적 로봇에서는 최소 외접 원을 자주 사용
#
# 색상 마스크
# → Contour 검출
# → 최소 외접 원 계산
# → 중심 좌표와 반지름 발행
# → 로봇이 공을 따라감
#
# 반지름은 객체가 카메라에 얼마나 가까운지 추정하는 데도 사용 가능
#
# 반지름 큼 → 가까움
# 반지름 작음 → 멀리 있음
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
    # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    # 기준값을 이용해 이미지를 흰색과 검은색의 이진 이미지로 분할
    ret, binary = cv2.threshold(
        blurred,
        127,
        255,
        cv2.THRESH_BINARY
    )

    # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
    contours, hierarchy = cv2.findContours(
        binary,
        cv2.RETR_EXTERNAL,
        cv2.CHAIN_APPROX_SIMPLE
    )

    # 원본이 바뀌지 않도록 이미지 배열의 독립적인 복사본을 생성
    result = image.copy()
    # min area 값을 계산하거나 저장해 이후 처리에서 사용
    min_area = 500

    # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
    for contour in contours:
        # 윤곽선이 차지하는 픽셀 면적을 계산
        area = cv2.contourArea(contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if area > min_area:
            # 윤곽선을 모두 포함하는 가장 작은 원의 중심과 반지름을 구함
            (x, y), radius = cv2.minEnclosingCircle(contour)

            # center 값을 계산하거나 저장해 이후 처리에서 사용
            center = (int(x), int(y))
            # radius 값을 계산하거나 저장해 이후 처리에서 사용
            radius = int(radius)

            # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
            cv2.circle(
                result,
                center,
                radius,
                (0, 255, 255),
                2
            )

            # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
            cv2.circle(
                result,
                center,
                5,
                (0, 0, 255),
                -1
            )

            # 현재 상태 또는 계산 결과의 터미널 출력
            print("중심:", center, "반지름:", radius)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Min Enclosing Circle", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
