# ============================================================================
# 노션 원문 학습 설명: 예제 71. 이미지 히스토그램
# ============================================================================
#
# [핵심 주제]
# 히스토그램은 이미지의 픽셀 밝기 값이 얼마나 분포되어 있는지 보여주는 그래프임
#
# 흑백 이미지 기준으로 픽셀 값은 보통 0~255임
#
# 0   = 검정
# 255 = 흰색
# 중간값 = 회색
#
# 히스토그램을 보면 이미지가 어두운지, 밝은지, 대비가 약한지 확인 가능
#
# [실습 목표]
# 1. Grayscale 이미지로 변환
# 2. cv2.calcHist() 사용법 이해
# 3. 밝기 분포 계산
# 4. matplotlib로 히스토그램 표시
#
# [실무에서 자주 하는 실수]
# 실수 1. OpenCV BGR 이미지를 matplotlib에 그대로 표시함
#
# 이 예제에서는 히스토그램만 그리므로 큰 문제는 없지만, 컬러 이미지를 matplotlib로 표시할 때는 BGR/RGB 변환이 필요
#
# rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# plt.imshow(rgb)
#
# 실수 2. 히스토그램만 보고 모든 것을 판단함
#
# 히스토그램은 밝기 분포를 보여주지만, 객체 위치나 모양은 알려주지 않습니다.
#
# 따라서 히스토그램은 보조 분석 도구로 사용필요
#
# [ROS2와 연결되는 포인트]
# ROS2 카메라 영상이 너무 어둡거나 너무 밝을 때 히스토그램을 보면 원인을 파악하기 쉽습니다.
#
# 히스토그램이 왼쪽에 몰림 → 전체적으로 어두움
# 히스토그램이 오른쪽에 몰림 → 전체적으로 밝음
# 히스토그램이 좁게 몰림 → 대비가 낮음
# 히스토그램이 넓게 퍼짐 → 대비가 높음
#
# 로봇 카메라 전처리 튜닝에서 중요한 진단 도구임
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 그래프나 이미지를 화면에 표시하기 위해 Matplotlib 기능을 불러오기
import matplotlib.pyplot as plt

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

    # 픽셀 밝기나 색상 값이 얼마나 분포하는지 히스토그램을 계산
    hist = cv2.calcHist(
        [gray],
        [0],
        None,
        [256],
        [0, 256]
    )

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Gray Image", gray)

    plt.figure()
    plt.title("Grayscale Histogram")
    plt.xlabel("Pixel Value")
    plt.ylabel("Pixel Count")
    plt.plot(hist)
    plt.xlim([0, 256])
    plt.show()

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
