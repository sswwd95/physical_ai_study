# ============================================================================
# 노션 원문 학습 설명: 예제 39. 이미지 스무딩 비교
# ============================================================================
#
# [핵심 주제]
# 평균 블러, Gaussian Blur, Median Blur, Bilateral Filter를 한 번에 비교
#
# 필터마다 장단점이 다르므로 상황에 맞게 선택필요
#
# [실습 목표]
# 1. 여러 필터 결과 비교
# 2. 각 필터의 특징 이해
# 3. 노이즈 종류별 적합한 필터 선택
# 4. 실무에서 필터 선택 기준 만들기
#
# [실무에서 자주 하는 실수]
# 실수 1. 필터를 많이 적용할수록 좋다고 생각함
#
# 필터를 여러 번 적용하면 이미지 정보가 점점 사라질 수 있음
#
# 원본
# → Blur
# → Blur
# → Blur
# → 객체 경계 약화
# → 검출 실패
#
# 필터는 필요한 만큼만 적용필요
#
# 실수 2. 필터 성능을 눈으로만 판단함
#
# 사람 눈에 보기 좋아진 이미지가 알고리즘 성능도 좋아진다는 보장은 없음
#
# 다음 기준으로 판단필요
#
# Contour 개수가 안정적인가?
# 객체 중심 좌표가 덜 흔들리는가?
# FPS가 충분한가?
# 오검출이 줄었는가?
#
# [ROS2와 연결되는 포인트]
# ROS2 비전 노드에서는 필터 선택이 곧 실시간 성능과 연결됨
#
# 필터 강함
# → 노이즈 감소
# → 검출 안정 가능
# → 계산량 증가
# → FPS 감소 가능
#
# 실무에서는 항상 다음 균형을 봐야 함
#
# 정확도 vs 속도
# 안정성 vs 지연시간
# 화질 vs 제어 반응성
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
    # 주변 픽셀의 평균값을 사용해 이미지를 부드럽게 생성
    average_blur = cv2.blur(image, (7, 7))
    # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
    gaussian_blur = cv2.GaussianBlur(image, (7, 7), 0)
    # 주변 픽셀의 중앙값을 사용해 Salt & Pepper 노이즈를 줄임
    median_blur = cv2.medianBlur(image, 7)
    # 경계선은 최대한 보존하면서 이미지의 노이즈를 줄임
    bilateral = cv2.bilateralFilter(image, 9, 75, 75)

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Average Blur", average_blur)
    cv2.imshow("Gaussian Blur", gaussian_blur)
    cv2.imshow("Median Blur", median_blur)
    cv2.imshow("Bilateral Filter", bilateral)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
