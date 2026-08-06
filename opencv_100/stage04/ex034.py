# ============================================================================
# 노션 원문 학습 설명: 예제 34. Bilateral Filter
# ============================================================================
#
# [핵심 주제]
# Bilateral Filter는 이미지를 부드럽게 하면서도 경계선은 최대한 유지하려는 필터임
#
# 일반 블러는 노이즈를 줄이지만 객체 경계도 흐리게 생성
#
# Bilateral Filter는 다음 목적에 사용됨
#
# 노이즈는 줄이고
# 객체 경계는 보존한다
#
# [실습 목표]
# 1. Bilateral Filter 개념 이해
# 2. cv2.bilateralFilter() 사용법 이해
# 3. Edge 보존 필터의 필요성 이해
# 4. 일반 블러와 차이 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. Bilateral Filter를 실시간 영상에 과도하게 사용
#
# Bilateral Filter는 품질이 좋지만 Gaussian Blur보다 계산량이 큽니다.
#
# 실시간 ROS2 카메라 노드에서는 FPS가 떨어질 수 있음
#
# 실수 2. sigma 값을 무작정 크게 설정
#
# 값을 크게 하면 노이즈는 줄어들 수 있지만, 이미지가 비현실적으로 뭉개질 수 있음
#
# 처음에는 다음 정도로 시작하는 것이 좋습니다.
#
# cv2.bilateralFilter(image, 9, 75, 75)
#
# [ROS2와 연결되는 포인트]
# Bilateral Filter는 객체 경계를 유지해야 하는 작업에서 유용
#
# 1. 물체 윤곽 검출
# 2. 부품 경계선 유지
# 3. 사람/장애물 영역 보존
# 4. Edge 기반 객체 검출 전처리
#
# 다만 로봇 주행처럼 빠른 반응이 필요한 경우에는 Gaussian Blur가 더 현실적인 선택일 수 있음
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
    # 경계선은 최대한 보존하면서 이미지의 노이즈를 줄임
    bilateral = cv2.bilateralFilter(
        image,
        d=9,
        sigmaColor=75,
        sigmaSpace=75
    )

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Bilateral Filter", bilateral)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
