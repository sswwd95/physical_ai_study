# ============================================================================
# 노션 원문 학습 설명: 예제 48. 다각형 근사
# ============================================================================
#
# [핵심 주제]
# 다각형 근사는 복잡한 Contour를 단순한 점들의 집합으로 줄이는 방법임
#
# 예를 들어 사각형 물체의 외곽선은 많은 점으로 구성될 수 있지만, 다각형 근사를 하면 꼭짓점 4개로 표현 가능
#
# [실습 목표]
# 1. cv2.arcLength() 사용법 이해
# 2. cv2.approxPolyDP() 사용법 이해
# 3. 꼭짓점 개수 확인
# 4. 단순화된 도형 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. 근사 계수를 고정하고 모든 이미지에 사용
#
# 0.02*perimeter
#
# 이 값은 좋은 시작점이지만, 객체 크기나 노이즈에 따라 조정이 필요
#
# 실수 2. 꼭짓점 개수만으로 도형을 무조건 판단
#
# 사각형처럼 보이는 물체도 노이즈 때문에 꼭짓점이 5개 이상 나올 수 있음
#
# 도형 분류에서는 꼭짓점 개수뿐 아니라 면적, 비율, 원형도 등을 함께 봐야 함
#
# [ROS2와 연결되는 포인트]
# 다각형 근사는 다음 작업에 유용
#
# 1. 사각형 마커 검출
# 2. 작업물 형태 분류
# 3. 박스형 장애물 검출
# 4. ArUco/QR 후보 영역 탐색
#
# ROS2 로봇 팔 프로젝트에서는 작업대 위 사각형 부품 후보를 찾는 데 사용 가능
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

    # 두 개의 임계값을 사용하는 Canny 알고리즘으로 안정적인 경계선을 찾습니다.
    edges = cv2.Canny(blurred, 50, 150)

    # 이진 이미지에서 연결된 흰색 영역의 외곽선 목록을 찾습니다.
    contours, hierarchy = cv2.findContours(
        edges,
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
            # 윤곽선의 둘레 길이를 계산
            perimeter = cv2.arcLength(contour, True)

            # 복잡한 윤곽선을 꼭짓점 수가 적은 다각형으로 단순화함
            approx = cv2.approxPolyDP(
                contour,
                0.02 * perimeter,
                True
            )

            # 검출한 윤곽선을 결과 이미지 위에 그리기
            cv2.drawContours(
                result,
                [approx],
                -1,
                (0, 255, 0),
                2
            )

            # 현재 상태 또는 계산 결과의 터미널 출력
            print("꼭짓점 개수:", len(approx))

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Edges", edges)
    cv2.imshow("Polygon Approximation", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
