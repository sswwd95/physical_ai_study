# ============================================================================
# 노션 원문 학습 설명: 예제 44. Contour 검출
# ============================================================================
#
# [핵심 주제]
# Contour는 이미지에서 같은 값으로 이어진 외곽선임
#
# 쉽게 말하면 객체의 테두리 선임
#
# Contour를 사용하면 객체의 위치, 크기, 모양, 중심점을 계산할 수 있음
#
# [실습 목표]
# 1. Contour 개념 이해
# 2. Threshold로 이진 이미지 생성
# 3. cv2.findContours() 사용법 이해
# 4. cv2.drawContours()로 외곽선 그리기
#
# [실무에서 자주 하는 실수]
# 실수 1. 이진화 없이 Contour 검출
#
# `findContours()`는 일반적으로 이진 이미지에서 사용해야 합니다.
#
# 권장 흐름은 다음임
#
# BGR
# → Grayscale
# → Threshold 또는 Canny
# → findContours
#
# 실수 2. 너무 많은 작은 Contour가 검출됨
#
# 노이즈가 많으면 작은 Contour가 많이 발생
#
# 이때는 다음 처리가 필요
#
# Blur
# Threshold 조정
# Morphology
# 면적 기준 필터링
#
# 면적 기준 필터링은 다음 예제에서 다룹니다.
#
# [ROS2와 연결되는 포인트]
# Contour는 로봇 비전에서 매우 중요
#
# 색상 마스크
# → Contour 검출
# → 가장 큰 Contour 선택
# → Bounding Box 계산
# → 중심 좌표 계산
# → ROS2 Topic 발행
#
# 예를 들어 파란 공을 추적하는 로봇은 파란색 마스크에서 Contour를 검출한 뒤 가장 큰 Contour를 목표 객체로 선택
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

    # 검출한 윤곽선을 결과 이미지 위에 그리기
    cv2.drawContours(
        result,
        contours,
        -1,
        (0, 0, 255),
        2
    )

    # 현재 상태 또는 계산 결과의 터미널 출력
    print("검출된 Contour 개수:", len(contours))

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Binary Image", binary)
    cv2.imshow("Contour Result", result)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
