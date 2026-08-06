# ============================================================================
# 노션 원문 학습 설명: 예제 23. 이미지 회전
# ============================================================================
#
# [핵심 주제]
# 이미지를 원하는 각도로 회전함
#
# 로봇 카메라가 약간 기울어져 장착되어 있거나, 이미지를 정렬해야 할 때 사용
#
# [실습 목표]
# 1. 회전 중심점 설정
# 2. cv2.getRotationMatrix2D() 이해
# 3. cv2.warpAffine() 사용
# 4. 이미지 회전 결과 확인
#
# [실무에서 자주 하는 실수]
# 실수 1. 회전 후 이미지가 잘림
#
# 이미지를 회전하면 모서리 부분이 잘릴 수 있음
#
# 이유는 출력 크기를 원본과 동일하게 지정했기 때문임
#
# rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))
#
# 정확히 모든 영역을 보존하려면 회전 후 필요한 출력 크기를 다시 계산필요
#
# 실수 2. center 좌표 순서를 헷갈림
#
# 회전 중심점은 다음 순서임
#
# center = (x, y)
#
# 이미지 shape는 다음 순서임
#
# height, width = image.shape[:2]
#
# 따라서 중앙점은 다음처럼 써야 함
#
# center = (width // 2, height // 2)
#
# [ROS2와 연결되는 포인트]
# 로봇 카메라가 실제 장착 과정에서 약간 비뚤어지는 경우가 있음
#
# 카메라가 왼쪽으로 5도 기울어짐
# 카메라가 오른쪽으로 10도 기울어짐
#
# 이때 소프트웨어적으로 회전 보정을 할 수 있음
#
# 카메라 프레임
# → 회전 보정
# → 라인 검출
# → 중심 좌표 계산
#
# 하지만 가능하면 하드웨어 장착을 먼저 정확히 맞추는 것이 좋습니다.
#
# 소프트웨어 보정은 추가 계산량과 이미지 손실을 만들 수 있음
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
    # 이미지 배열의 높이, 너비, 채널 수 같은 크기 정보를 가져옵니다.
    height, width = image.shape[:2]

    # center 값을 계산하거나 저장해 이후 처리에서 사용
    center = (width // 2, height // 2)
    # angle 변수에 이후 처리에 사용할 값을 저장
    angle = 30
    # scale 변수에 이후 처리에 사용할 값을 저장
    scale = 1.0

    # 이미지를 회전시키는 데 필요한 2×3 변환 행렬을 계산
    rotation_matrix = cv2.getRotationMatrix2D(center, angle, scale)

    # 이동·회전·기울이기 같은 Affine 변환을 이미지에 적용
    rotated_image = cv2.warpAffine(image, rotation_matrix, (width, height))

    # 처리 결과 확인용 OpenCV 창 표시
    cv2.imshow("Original Image", image)
    cv2.imshow("Rotated Image", rotated_image)

    # 키 입력 대기 및 실시간 영상 갱신
    cv2.waitKey(0)
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
