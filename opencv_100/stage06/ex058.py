# ============================================================================
# 노션 원문 학습 설명: 예제 58. 실시간 흑백 변환
# ============================================================================
#
# [핵심 주제]
# 카메라 프레임을 실시간으로 Grayscale 이미지로 변환
#
# [실습 목표]
# 1. 실시간 프레임 처리 구조 복습
# 2. cv2.cvtColor() 실시간 적용
# 3. 컬러 영상과 흑백 영상 동시 출력
# 4. ROS2 비전 전처리 흐름 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. 흑백 이미지에 색상 검출을 하려고 함
#
# 흑백 이미지에는 색상 정보가 없음
#
# 색상 검출은 HSV 변환을 사용필요
#
# 실수 2. 흑백 변환 후 shape를 3개로 받음
#
# 흑백 이미지는 보통 2차원임
#
# height, width = gray.shape
#
# 컬러 이미지처럼 다음을 쓰면 오류가 날 수 있음
#
# height, width, channels = gray.shape
#
# [ROS2와 연결되는 포인트]
# ROS2 카메라 Subscriber에서 가장 흔한 전처리 중 하나가 흑백 변환임
#
# /camera/image_raw
# → cv_bridge
# → BGR frame
# → Grayscale
# → Threshold / Edge
#
# 라인 트레이싱, Edge 검출, Contour 분석의 시작점임
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

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Original Camera", frame)
        cv2.imshow("Gray Camera", gray)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
