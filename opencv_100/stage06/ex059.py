# ============================================================================
# 노션 원문 학습 설명: 예제 59. 실시간 Edge 검출
# ============================================================================
#
# [핵심 주제]
# 카메라 프레임에 실시간으로 Canny Edge를 적용
#
# [실습 목표]
# 1. 실시간 Grayscale 변환
# 2. 실시간 Gaussian Blur
# 3. 실시간 Canny Edge 검출
# 4. Edge 결과 화면 출력
#
# [실무에서 자주 하는 실수]
# 실수 1. Canny 임계값을 상황에 맞게 조정하지 않음
#
# 조명이 어두우면 Edge가 적게 나오고, 노이즈가 많으면 Edge가 너무 많이 나올 수 있음
#
# 다음 값들을 실험해 봅니다.
#
# edges = cv2.Canny(blurred, 30, 100)
# edges = cv2.Canny(blurred, 50, 150)
# edges = cv2.Canny(blurred, 100, 200)
#
# 실수 2. 실시간 처리 속도 확인을 하지 않음
#
# Edge 처리를 넣으면 FPS가 떨어질 수 있음
#
# 실무에서는 예제 55의 FPS 표시와 함께 사용해 성능을 확인하는 것이 좋습니다.
#
# [ROS2와 연결되는 포인트]
# ROS2 비전 노드에서 Edge 결과를 별도 이미지 토픽으로 발행할 수 있음
#
# /camera/image_raw
# → OpenCV Canny 처리
# → /camera/edge_image Publish
#
# RViz2나 rqt_image_view에서 처리 결과를 확인하면 디버깅이 쉬워집니다.
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 열기
cap = cv2.VideoCapture(0)

# 카메라나 동영상 입력이 정상적으로 열렸는지 확인
if not cap.isOpened():
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("카메라를 열 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # 조건이 참인 동안 아래 코드를 계속 반복
    while True:
        # 영상에서 프레임 한 장을 읽고, 성공 여부와 이미지 배열을 각각 수신
        ret, frame = cap.read()

        # 필요한 조건이 충족되지 않았을 때의 처리를 시작함
        if not ret:
            # 현재 상태 또는 계산 결과의 터미널 출력
            print("프레임을 읽을 수 없습니다.")
            # 현재 반복문을 즉시 종료
            break

        # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 두 개의 임계값을 사용하는 Canny 알고리즘으로 안정적인 경계선을 찾습니다.
        edges = cv2.Canny(blurred, 50, 150)

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Original Camera", frame)
        cv2.imshow("Canny Edge Camera", edges)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
