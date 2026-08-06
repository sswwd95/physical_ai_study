# ============================================================================
# 노션 원문 학습 설명: 예제 60. 카메라 프레임 캡처
# ============================================================================
#
# [핵심 주제]
# 실시간 카메라 영상에서 특정 키를 눌렀을 때 현재 프레임을 이미지 파일로 저장
#
# [실습 목표]
# 1. 실시간 프레임 저장
# 2. s 키로 캡처
# 3. 파일 이름 자동 증가
# 4. 데이터셋 수집 기초 이해
#
# [실무에서 자주 하는 실수]
# 실수 1. 저장 폴더를 만들지 않음
#
# 저장 경로의 폴더가 없으면 `cv2.imwrite()`가 실패할 수 있음
#
# os.makedirs(save_dir, exist_ok=True)
#
# 를 반드시 사용
#
# 실수 2. 같은 파일명으로 계속 덮어씀
#
# 다음처럼 쓰면 매번 같은 파일을 덮어씁니다.
#
# cv2.imwrite("capture.jpg", frame)
#
# 데이터셋 수집에서는 번호나 시간 기반 파일명을 사용필요
#
# [ROS2와 연결되는 포인트]
# 카메라 프레임 캡처는 ROS2 실습에서 매우 자주 필요
#
# 1. 라인트레이싱 학습 이미지 수집
# 2. 객체 인식 학습 데이터셋 수집
# 3. 장애물 검출 실패 장면 저장
# 4. 로봇 팔 Pick 위치 샘플 이미지 저장
# 5. 알고리즘 디버깅용 프레임 저장
#
# ROS2 카메라 노드에서도 같은 개념으로 특정 조건에서 프레임을 저장할 수 있음
#
# 객체 검출 실패
# → 현재 프레임 저장
# → 나중에 원인 분석
#
# # 6단계 핵심 정리
#
# 이번 6단계에서는 카메라와 비디오 처리의 핵심 문법을 배웠습니다.
#
# | 예제 | 핵심 내용 |
# | --- | --- |
# | 51 | 웹캠 열기 |
# | 52 | 실시간 프레임 출력 |
# | 53 | 키보드 입력 처리 |
# | 54 | 카메라 해상도 설정 |
# | 55 | FPS 확인 |
# | 56 | 비디오 파일 읽기 |
# | 57 | 비디오 저장 |
# | 58 | 실시간 흑백 변환 |
# | 59 | 실시간 Edge 검출 |
# | 60 | 카메라 프레임 캡처 |
#
# # 초보자가 반드시 기억해야 할 핵심 문법
#
# cap = cv2.VideoCapture(0)
#
# 기본 웹캠을 열기
#
# ret, frame = cap.read()
#
# 카메라에서 한 프레임을 읽기
#
# if not cap.isOpened():
# print("카메라를 열 수 없습니다.")
#
# 카메라 열기 성공 여부를 확인
#
# cv2.imshow("Camera", frame)
#
# 프레임을 화면에 출력
#
# key = cv2.waitKey(1)
#
# 실시간 영상에서 키 입력을 수신
#
# if key == ord('q'):
# break
#
# `q` 키로 종료합니다.
#
# cap.release()
# cv2.destroyAllWindows()
#
# 카메라와 창을 정리함
#
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
#
# 카메라 해상도를 설정
#
# gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
# 실시간 프레임을 흑백으로 변환
#
# edges = cv2.Canny(blurred, 50, 150)
#
# 실시간 Edge를 검출
#
# cv2.imwrite(file_path, frame)
#
# 현재 프레임을 이미지로 저장
#
# # ROS2 Humble 강의 전 관점에서 중요한 이유
#
# 이번 단계는 OpenCV 단독 실습에서 ROS2 비전 노드로 넘어가는 연결 다리임
#
# OpenCV 실시간 구조는 다음과 같습니다.
#
# VideoCapture
# → frame 읽기
# → OpenCV 처리
# → imshow
#
# ROS2 구조는 다음과 같습니다.
#
# /camera/image_raw Subscribe
# → cv_bridge
# → OpenCV frame 변환
# → OpenCV 처리
# → 결과 Publish
#
# 즉, 이번 단계에서 배운 `frame` 처리 방식은 ROS2에서도 거의 그대로 사용됨
#
# # 실무 기준 처리 흐름 예시
# ============================================================================
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2
# 파일과 폴더 경로를 안전하게 다루기 위한 기능을 불러오기
import os

# save dir 변수에 이후 처리에 사용할 값을 저장
save_dir = "captured_images"
os.makedirs(save_dir, exist_ok=True)

# 웹캠 번호 또는 동영상 파일을 OpenCV 영상 입력으로 열기
cap = cv2.VideoCapture(0)

# 카메라나 동영상 입력이 정상적으로 열렸는지 확인
if not cap.isOpened():
    # 현재 상태 또는 계산 결과의 터미널 출력
    print("카메라를 열 수 없습니다.")
# 앞 조건이 거짓일 때의 실행 구간
else:
    # count 값을 계산하거나 저장해 이후 처리에서 사용
    count = 0

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

        # 처리 결과 확인용 OpenCV 창 표시
        cv2.imshow("Capture Camera", frame)

        # 키 입력 대기 및 실시간 영상 갱신
        key = cv2.waitKey(1)

        # 조건이 참일 때만 아래 들여쓰기된 코드를 실행
        if key == ord('s'):
            # file path 변수에 이후 처리에 사용할 값을 저장
            file_path = os.path.join(save_dir, f"capture_{count:04d}.jpg")
            # 현재 이미지 배열을 지정한 경로의 이미지 파일로 저장
            cv2.imwrite(file_path, frame)
            # 현재 상태 또는 계산 결과의 터미널 출력
            print("이미지 저장:", file_path)
            count += 1

        # 앞 조건이 거짓일 때 추가 조건을 검사함
        elif key == ord('q'):
            # 현재 상태 또는 계산 결과의 터미널 출력
            print("프로그램 종료")
            # 현재 반복문을 즉시 종료
            break

    # 카메라·동영상·VideoWriter 자원을 운영체제에 반환
    cap.release()
    # 모든 OpenCV 이미지 창 닫기
    cv2.destroyAllWindows()
