# ============================================================================
# 노션 원문 학습 설명: 예제 3. 이미지 화면 출력
# ============================================================================
#
# [핵심 주제]
# `cv2.imshow()`를 사용해 이미지를 화면에 출력합니다.
#
# [실습 목표]
# 1. OpenCV 창 띄우기
# 2. 이미지 화면 출력
# 3. 키 입력 대기
# 4. 창 닫기
#
# [실무에서 자주 하는 실수]
# 실수 1. waitKey를 빼먹음
#
# 다음처럼 작성하면 창이 나타났다가 바로 사라질 수 있음
#
# cv2.imshow("Sample Image",image)
# cv2.destroyAllWindows()
#
# 반드시 `cv2.waitKey()`가 필요
#
# 실수 2. 원격 Docker 환경에서 imshow 사용
#
# Docker, WSL2, SSH 환경에서는 GUI 창이 바로 뜨지 않을 수 있음
#
# ROS2 Docker 실습에서는 다음 같은 대안이 필요
#
# 1. X11 설정
# 2. VcXsrv 사용
# 3. 이미지 파일로 저장 후 확인
# 4. Jupyter Notebook에서는 matplotlib 사용
#
# [ROS2와 연결되는 포인트]
# ROS2에서 카메라 영상을 디버깅할 때 가장 쉬운 방법 중 하나가 `cv2.imshow()`임
#
# 예를 들어 카메라 Subscriber 노드에서 다음처럼 사용 가능
#
# cv2.imshow("camera", frame)
# cv2.waitKey(1)
#
# 실시간 카메라에서는 `waitKey(0)`이 아니라 보통 `waitKey(1)`을 사용
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
    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Sample Image", image)
    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
