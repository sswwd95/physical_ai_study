# ============================================================================
# 노션 원문 학습 설명: 예제 57. 비디오 저장
# ============================================================================
#
# [핵심 주제]
# 카메라 또는 비디오 프레임을 처리한 뒤 결과를 새 비디오 파일로 저장
#
# [실습 목표]
# 1. cv2.VideoWriter() 사용법 이해
# 2. 코덱 설정
# 3. 영상 크기와 FPS 설정
# 4. 처리 결과 영상 저장
#
# [실무에서 자주 하는 실수]
# 실수 1. 저장 프레임 크기와 실제 프레임 크기가 다름
#
# `VideoWriter`에 설정한 크기와 실제 `frame` 크기가 다르면 저장이 제대로 안 될 수 있습니다.
#
# 실수 2. out.release()를 빼먹음
#
# 비디오 저장 후 반드시 호출필요
#
# out.release()
#
# [ROS2와 연결되는 포인트]
# ROS2 로봇 실험에서는 결과 영상을 저장하는 기능이 매우 유용
#
# 주행 실험 기록
# 객체 검출 실패 장면 분석
# 알고리즘 개선 전후 비교
# 학습 데이터 수집
#
# ROS2에서는 rosbag으로 토픽을 저장할 수도 있지만, OpenCV로 처리 결과 영상을 저장하면 시각적으로 바로 확인하기 좋습니다.
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
    # 카메라나 동영상의 속성값을 읽기
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # fps 값을 계산하거나 저장해 이후 처리에서 사용
    fps = 20.0

    # 저장할 동영상의 압축 코덱을 지정
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    # 처리한 프레임을 동영상 파일로 저장할 VideoWriter를 생성
    out = cv2.VideoWriter(
        "output_camera.mp4",
        fourcc,
        fps,
        (width, height)
    )

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

        # 현재 프레임을 출력 동영상에 한 장 추가
        out.write(frame)

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Recording Camera", frame)

        # 키 입력 대기 및 실시간 영상 갱신
        if cv2.waitKey(1) == ord('q'):
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    out.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
