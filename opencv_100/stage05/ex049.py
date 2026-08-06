# ============================================================================
# 노션 원문 학습 설명: 예제 49. 도형 분류
# ============================================================================
#
# [핵심 주제]
# Contour와 다각형 근사를 이용해 도형을 분류함
#
# 이번 예제에서는 단순하게 꼭짓점 개수로 다음 도형을 분류함
#
# 삼각형
# 사각형
# 원 또는 기타 도형
#
# [실습 목표]
# 1. Contour 기반 도형 분류 흐름 이해
# 2. 꼭짓점 개수 기반 분류
# 3. Bounding Box와 텍스트 표시
# 4. cv2.putText() 사용법 이해
#
# [준비 파일]
# 이 예제는 여러 도형이 들어 있는 이미지가 있으면 좋습니다.
#
# practice_images/shapes.png
#
# 예를 들어 흰 배경에 검은색 삼각형, 사각형, 원이 있는 이미지를 사용하면 이해하기 쉽습니다.
#
# [실무에서 자주 하는 실수]
# 실수 1. 도형 색과 배경 색을 고려하지 않음
#
# 검은 도형이 흰 배경에 있으면 이진화 결과에서 배경이 흰색이 되어 Contour가 이상하게 잡힐 수 있음
#
# 이때는 다음을 사용
#
# cv2.THRESH_BINARY_INV
#
# 실수 2. 원을 꼭짓점 개수만으로 판단
#
# 원도 다각형 근사 결과에 따라 꼭짓점이 8개, 10개, 20개 등으로 나올 수 있음
#
# 정확한 원 판단에는 원형도 계산을 추가하는 것이 좋습니다.
#
# 원형도 = 4π × 면적 / 둘레²
#
# 초보 단계에서는 꼭짓점 개수 기반 분류만 익혀도 충분함
#
# [ROS2와 연결되는 포인트]
# 도형 분류는 로봇 비전의 기초 규칙 기반 인식임
#
# 카메라 이미지
# → 이진화
# → Contour
# → 다각형 근사
# → 도형 분류
# → ROS2 메시지로 shape_name 발행
#
# 예를 들어 교육용 로봇 팔이 다음처럼 동작할 수 있음
#
# 삼각형이면 왼쪽 박스에 분류
# 사각형이면 오른쪽 박스에 분류
# 원형이면 중앙 박스에 분류
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 입력 또는 출력 파일 경로 지정
image_path = "practice_images/shapes.png"

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

    # 기준값을 이용해 이미지를 흰색과 검은색의 이진 이미지로 분할
    ret, binary = cv2.threshold(
        gray,
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
    min_area = 300

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

            # vertices 변수에 이후 처리에 사용할 값을 저장
            vertices = len(approx)

            # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
            if vertices == 3:
                # shape name 변수에 이후 처리에 사용할 값을 저장
                shape_name = "Triangle"
            # 앞 조건이 거짓일 때 추가 조건을 검사함
            elif vertices == 4:
                # shape name 변수에 이후 처리에 사용할 값을 저장
                shape_name = "Rectangle"
            # 앞 조건이 거짓일 때의 실행 구간
            else:
                # shape name 변수에 이후 처리에 사용할 값을 저장
                shape_name = "Circle or Other"

            # 윤곽선을 감싸는 축에 평행한 사각형의 위치와 크기를 계산
            x, y, w, h = cv2.boundingRect(approx)

            # 검출한 윤곽선을 결과 이미지 위에 그리기
            cv2.drawContours(
                result,
                [approx],
                -1,
                (0, 255, 0),
                2
            )

            # 이미지 위에 상태나 좌표 정보를 글자로 표시
            cv2.putText(
                result,
                shape_name,
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.6,
                (0, 0, 255),
                2
            )

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Shape Classification", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
