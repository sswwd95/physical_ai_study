# ============================================================================
# 노션 원문 학습 설명: 예제 41. Sobel Edge
# ============================================================================
#
# [핵심 주제]
# Sobel Edge는 이미지에서 밝기 변화가 큰 부분을 찾아 Edge를 검출하는 방법임
#
# Edge는 쉽게 말하면 경계선임
#
# 밝은 영역과 어두운 영역이 급격히 바뀌는 부분
# 색 또는 밝기가 갑자기 변하는 부분
# 객체와 배경이 만나는 부분
#
# Sobel은 특히 x방향, y방향 변화량을 따로 계산할 수 있음
#
# [실습 목표]
# 1. Sobel Edge 개념 이해
# 2. x방향 Edge 검출
# 3. y방향 Edge 검출
# 4. x/y Edge 합성 결과 확인
#
# [실무에서 자주 하는 실수]
# 실수 1. Sobel 결과를 바로 imshow에 넣음
#
# Sobel 결과는 음수나 255를 넘는 값을 포함할 수 있음
#
# 그래서 다음 변환이 필요
#
# sobel_abs = cv2.convertScaleAbs(sobel)
#
# 실수 2. 노이즈 제거 없이 바로 Edge 검출
#
# 노이즈가 많은 이미지에 Sobel을 적용하면 작은 잡음도 Edge로 검출됨
#
# 보통 다음 흐름이 안정적임
#
# Grayscale
# → Gaussian Blur
# → Sobel
#
# [ROS2와 연결되는 포인트]
# Sobel은 다음 작업에 활용할 수 있음
#
# 1. 라인 방향성 분석
# 2. 객체 경계 검출
# 3. 바닥 패턴 변화 감지
# 4. 차선 후보 검출
#
# 다만 실제 객체 외곽선 추출에는 Canny Edge와 Contour 조합을 더 자주 사용
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

    # 가로 또는 세로 방향의 밝기 변화량을 계산해 경계선을 찾습니다.
    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    # 픽셀값이 0~255 범위를 벗어나지 않도록 안전하게 밝기·대비를 조절함
    sobel_x_abs = cv2.convertScaleAbs(sobel_x)
    sobel_y_abs = cv2.convertScaleAbs(sobel_y)

    # sobel combined 변수에 이후 처리에 사용할 값을 저장
    sobel_combined = cv2.addWeighted(
        sobel_x_abs,
        0.5,
        sobel_y_abs,
        0.5,
        0
    )

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Gray Image", gray)
    cv2.imshow("Sobel X", sobel_x_abs)
    cv2.imshow("Sobel Y", sobel_y_abs)
    cv2.imshow("Sobel Combined", sobel_combined)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
