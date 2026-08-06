# ============================================================================
# 노션 원문 학습 설명: 예제 50. 객체 중심점 계산
# ============================================================================
#
# [핵심 주제]
# 객체 중심점은 로봇 비전에서 가장 중요한 정보 중 하나임
#
# 로봇은 이미지 전체를 이해하는 것이 아니라, 보통 다음 좌표가 필요
#
# 객체 중심 x좌표
# 객체 중심 y좌표
# 화면 중앙과 객체 중심의 차이
#
# 이 정보를 이용해 로봇이 왼쪽으로 돌지, 오른쪽으로 돌지, 앞으로 갈지 결정할 수 있음
#
# [실습 목표]
# 1. cv2.moments() 사용법 이해
# 2. Contour 중심점 계산
# 3. 중심점 화면 표시
# 4. 로봇 제어와 연결되는 오차 계산
#
# [실무에서 자주 하는 실수]
# 실수 1. moments["m00"] 확인 없이 나눗셈
#
# 다음 코드는 위험함
#
# center_x = int(moments["m10"] / moments["m00"])
#
# 반드시 다음 조건을 확인필요
#
# if moments["m00"] != 0:
#
# 실수 2. 여러 객체가 있을 때 모두 중심을 계산함
#
# 목표 객체가 하나라면 보통 가장 큰 Contour만 선택
#
# largest_contour = max(contours, key=cv2.contourArea)
#
# 그 후 중심점을 계산하면 더 안정적임
#
# 실수 3. 이미지 좌표와 로봇 좌표를 바로 같다고 생각함
#
# 이미지 좌표계는 다음과 같습니다.
#
# x 증가 → 오른쪽
# y 증가 → 아래쪽
#
# 로봇 좌표계는 보통 다음과 다릅니다.
#
# x축 → 전방
# y축 → 좌우
# z축 → 위
#
# 따라서 이미지 중심 좌표를 로봇 실제 좌표로 바꾸려면 카메라 캘리브레이션과 좌표 변환이 필요
#
# [ROS2와 연결되는 포인트]
# 객체 중심점 계산은 ROS2 비전 제어의 핵심임
#
# 예를 들어 객체 추종 로봇은 다음 흐름을 사용
#
# /camera/image_raw
# → OpenCV 처리
# → 객체 중심 center_x 계산
# → 화면 중앙 image_center_x와 비교
# → error_x 계산
# → error_x가 음수면 왼쪽 회전
# → error_x가 양수면 오른쪽 회전
# → /cmd_vel Publish
#
# 간단한 제어 로직은 다음과 같이 생각할 수 있음
#
# if error_x < -30:
# print("왼쪽으로 회전")
# elif error_x > 30:
# print("오른쪽으로 회전")
# else:
# print("정면으로 이동")
#
# # 5단계 핵심 정리
#
# 이번 5단계에서는 이미지에서 객체의 경계와 모양을 분석하는 핵심 문법을 배웠습니다.
#
# | 예제 | 핵심 내용 |
# | --- | --- |
# | 41 | Sobel Edge |
# | 42 | Laplacian Edge |
# | 43 | Canny Edge |
# | 44 | Contour 검출 |
# | 45 | Contour 면적 계산 |
# | 46 | Bounding Box |
# | 47 | 최소 외접 원 |
# | 48 | 다각형 근사 |
# | 49 | 도형 분류 |
# | 50 | 객체 중심점 계산 |
#
# # 초보자가 반드시 기억해야 할 핵심 문법
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#
# Edge와 Contour 전처리를 위해 흑백 이미지로 변환
#
# blurred = cv2.GaussianBlur(gray, (5, 5), 0)
#
# Edge 검출 전에 노이즈를 줄임
#
# edges = cv2.Canny(blurred, 50, 150)
#
# Canny Edge를 검출
#
# contours, hierarchy = cv2.findContours(
# binary,
# cv2.RETR_EXTERNAL,
# cv2.CHAIN_APPROX_SIMPLE
# )
#
# Contour를 검출
#
# area = cv2.contourArea(contour)
#
# Contour 면적을 계산
#
# x, y, w, h = cv2.boundingRect(contour)
#
# Bounding Box를 계산
#
# cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
#
# 사각형 박스를 그리기
#
# (x, y), radius = cv2.minEnclosingCircle(contour)
#
# 최소 외접 원을 계산
#
# perimeter = cv2.arcLength(contour, True)
# approx = cv2.approxPolyDP(contour, 0.02 * perimeter, True)
#
# Contour를 다각형으로 근사함
#
# moments = cv2.moments(contour)
# center_x = int(moments["m10"] / moments["m00"])
# center_y = int(moments["m01"] / moments["m00"])
#
# 객체 중심점을 계산
#
# # ROS2 Humble 강의 전 관점에서 중요한 이유
#
# 이번 단계는 OpenCV가 ROS2 로봇 제어로 연결되는 핵심 구간임
#
# 카메라 영상
# → 전처리
# → Edge 또는 Threshold
# → Contour 검출
# → 객체 위치 계산
# → 중심점 계산
# → ROS2 Topic 발행
# → 로봇 제어
#
# 특히 다음 기능을 만들기 위한 기반임
#
# 라인 트레이싱
# 색상 공 추적
# 장애물 외곽선 검출
# 작업물 중심 좌표 계산
# 로봇 팔 Pick 위치 추정
# 컨베이어 객체 카운팅
#
# # 실무 기준 처리 흐름 예시
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

    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    height, width = image.shape[:2]
    # image center x 값을 계산하거나 저장해 이후 처리에서 사용
    image_center_x = width // 2

    # 기준선이나 검출 결과를 표시하기 위해 선을 그리기
    cv2.line(
        result,
        (image_center_x, 0),
        (image_center_x, height),
        (255, 0, 0),
        2
    )

    # 목록이나 범위의 항목을 하나씩 꺼내 같은 처리를 반복
    for contour in contours:
        # 윤곽선이 차지하는 픽셀 면적을 계산
        area = cv2.contourArea(contour)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if area > min_area:
            # 윤곽선의 면적과 중심점을 계산하는 데 필요한 모멘트 값을 구함
            moments = cv2.moments(contour)

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
            if moments["m00"] != 0:
                # center x 값을 계산하거나 저장해 이후 처리에서 사용
                center_x = int(moments["m10"] / moments["m00"])
                # center y 값을 계산하거나 저장해 이후 처리에서 사용
                center_y = int(moments["m01"] / moments["m00"])

                # error x 값을 계산하거나 저장해 이후 처리에서 사용
                error_x = center_x - image_center_x

                # 검출한 윤곽선을 결과 이미지 위에 그리기
                cv2.drawContours(
                    result,
                    [contour],
                    -1,
                    (0, 255, 0),
                    2
                )

                # 중심점이나 원형 객체를 표시하기 위해 원을 그리기
                cv2.circle(
                    result,
                    (center_x, center_y),
                    6,
                    (0, 0, 255),
                    -1
                )

                # 이미지 위에 상태나 좌표 정보를 글자로 표시
                cv2.putText(
                    result,
                    f"Center: ({center_x}, {center_y})",
                    (center_x + 10, center_y),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.5,
                    (0, 0, 255),
                    2
                )

                # 이미지 위에 상태나 좌표 정보를 글자로 표시
                cv2.putText(
                    result,
                    f"Error X: {error_x}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 255),
                    2
                )

                # 현재 상태 또는 계산 결과의 터미널 출력
                print("객체 중심:", center_x, center_y)
                print("화면 중앙 대비 x 오차:", error_x)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Object Center", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
