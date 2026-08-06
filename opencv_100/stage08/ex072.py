# ============================================================================
# 노션 원문 학습 설명: 예제 72. 히스토그램 평활화
# ============================================================================
#
# [핵심 주제]
# 히스토그램 평활화는 어둡거나 대비가 낮은 이미지를 더 선명하게 보이도록 밝기 분포를 넓게 펴는 기법임
#
# 특히 Grayscale 이미지에서 많이 사용
#
# [실습 목표]
# 1. cv2.equalizeHist() 사용법 이해
# 2. 대비 개선 효과 확인
# 3. 원본 히스토그램과 평활화 후 히스토그램 비교
# 4. 조명 보정 기초 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. 컬러 이미지에 equalizeHist를 바로 적용
#
# `cv2.equalizeHist()`는 1채널 이미지에 적용해야 합니다.
#
# 잘못된 예:
#
# equalized = cv2.equalizeHist(image)
#
# 올바른 예:
#
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# equalized = cv2.equalizeHist(gray)
#
# 실수 2. 평활화가 항상 좋은 결과를 만든다고 생각함
#
# 히스토그램 평활화는 노이즈도 함께 강조할 수 있음
#
# 어두운 이미지에서는 효과가 좋을 수 있지만, 노이즈가 많은 영상에서는 오히려 결과가 나빠질 수 있음
#
# [ROS2와 연결되는 포인트]
# 로봇 카메라가 어두운 실내에서 동작할 때 평활화는 Edge나 Threshold 검출을 도울 수 있음
#
# 카메라 프레임
# → Grayscale
# → Histogram Equalization
# → Threshold 또는 Canny
# → Contour
#
# 하지만 실시간 영상에서는 처리 결과가 프레임마다 흔들릴 수 있으므로 주의필요
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

    # 밝기 히스토그램을 고르게 펴서 이미지 대비를 높임
    equalized = cv2.equalizeHist(gray)

    # 픽셀 밝기나 색상 값이 얼마나 분포하는지 히스토그램을 계산
    hist_original = cv2.calcHist([gray], [0], None, [256], [0, 256])
    hist_equalized = cv2.calcHist([equalized], [0], None, [256], [0, 256])

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Gray", gray)
    cv2.imshow("Equalized Gray", equalized)

    plt.figure()
    plt.title("Histogram Comparison")
    plt.plot(hist_original, label="Original")
    plt.plot(hist_equalized, label="Equalized")
    plt.xlim([0, 256])
    plt.legend()
    plt.show()

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
