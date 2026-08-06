# ============================================================================
# 노션 원문 학습 설명: 예제 46. Bounding Box
# ============================================================================
#
# [핵심 주제]
# Bounding Box는 객체를 둘러싸는 사각형임
#
# Contour를 검출한 뒤 Bounding Box를 구하면 객체의 위치와 크기를 쉽게 알 수 있음
#
# [실습 목표]
# 1. cv2.boundingRect() 사용법 이해
# 2. 객체의 x, y, width, height 계산
# 3. cv2.rectangle()로 박스 그리기
# 4. 객체 위치 정보 추출
#
# [실무에서 자주 하는 실수]
# 실수 1. Bounding Box 중심 좌표 계산을 빼먹음
#
# Bounding Box가 있으면 중심 좌표는 다음처럼 계산할 수 있음
#
# center_x = x + w // 2
# center_y = y + h // 2
#
# 이 중심 좌표가 로봇 제어에 매우 중요
#
# 실수 2. Bounding Box 크기만 보고 실제 객체 크기라고 오해
#
# Bounding Box는 객체를 감싸는 사각형임
#
# 객체가 기울어져 있거나 둥글면 실제 객체 면적과 Bounding Box 면적은 다릅니다.
#
# [ROS2와 연결되는 포인트]
# Bounding Box는 객체 인식 결과를 표현할 때 매우 많이 사용
#
# 객체 검출
# → Bounding Box
# → 중심 좌표 계산
# → 화면 중앙과 비교
# → 로봇 회전 방향 결정
#
# 예를 들어 객체 중심이 화면 왼쪽에 있으면 로봇이 왼쪽으로 회전하도록 제어할 수 있음
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
            # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산
            x, y, w, h = cv2.boundingRect(contour)

            # 검출 영역을 알아보기 쉽도록 사각형을 그리기
            cv2.rectangle(
                result,
                (x, y),
                (x + w, y + h),
                (255, 0, 0),
                2
            )

            # 현재 상태 또는 계산 결과의 터미널 출력
            print("Bounding Box:", x, y, w, h)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Bounding Box Result", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
