# ============================================================================
# 노션 원문 학습 설명: 예제 45. Contour 면적 계산
# ============================================================================
#
# [핵심 주제]
# 검출된 Contour의 면적을 계산하고, 너무 작은 노이즈 Contour를 제거
#
# 실무에서는 모든 Contour가 의미 있는 객체가 아님
#
# 작은 점, 그림자, 반사, 노이즈도 Contour로 검출될 수 있음
#
# [실습 목표]
# 1. cv2.contourArea() 사용법 이해
# 2. Contour 면적 기준 필터링
# 3. 작은 노이즈 제거
# 4. 의미 있는 객체만 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. 면적 기준을 상황에 맞게 조정하지 않음
#
# 카메라 해상도에 따라 적절한 면적 기준은 변화
#
# 320×240 영상에서 area 500은 꽤 큰 객체
# 1920×1080 영상에서 area 500은 작은 노이즈일 수 있음
#
# 실수 2. 가장 큰 Contour를 무조건 목표 객체로 봄
#
# 색상 검출에서는 가장 큰 Contour가 목표일 가능성이 높지만, 항상 그런 것은 아님
#
# 예를 들어 배경에 같은 색의 큰 물체가 있으면 잘못 선택할 수 있음
#
# [ROS2와 연결되는 포인트]
# 로봇 비전에서는 면적 기준 필터링이 매우 중요
#
# 색상 마스크
# → Contour 검출
# → 면적이 너무 작은 것 제거
# → 가장 큰 객체 선택
# → 중심 좌표 계산
#
# 이렇게 해야 로봇이 작은 노이즈를 목표로 잘못 추적하지 않습니다.
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
            # 검출한 윤곽선을 결과 이미지 위에 그리기
            cv2.drawContours(
                result,
                [contour],
                -1,
                (0, 255, 0),
                2
            )
            # 현재 상태 또는 계산 결과의 터미널 출력
            print("검출된 객체 면적:", area)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Filtered Contours", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
