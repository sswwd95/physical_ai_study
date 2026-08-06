# ============================================================================
# 노션 원문 학습 설명: 예제 85. 카메라 노드 구조 설계
# ============================================================================
#
# [핵심 주제]
# ROS2에서 OpenCV 카메라 처리 노드를 만들 때는 기능을 구조적으로 나누어야 함
#
# 초보자는 모든 코드를 콜백 안에 넣는 경우가 많습니다.
#
# 하지만 실무에서는 다음처럼 역할을 분리하는 것이 좋습니다.
#
# 입력 수신
# 변환
# 처리
# 결과 생성
# 발행
# 디버깅 표시
#
# [실습 목표]
# 1. ROS2 비전 노드 기본 구조 이해
# 2. image_callback 역할 이해
# 3. process_frame() 함수 분리
# 4. publish_result() 함수 분리
#
# [실무에서 자주 하는 실수]
# 실수 1. 콜백 함수가 너무 커짐
#
# 나쁜 구조는 다음과 같습니다.
#
# image_callback 안에
# 변환
# 전처리
# 검출
# 좌표 계산
# 이미지 발행
# 문자열 발행
# 로그
# 디버깅 표시
# 전부 들어감
#
# 이렇게 되면 오류가 났을 때 어디가 문제인지 찾기 어렵습니다.
#
# 실수 2. OpenCV 코드와 ROS2 코드를 분리하지 않음
#
# OpenCV 처리 함수는 가능하면 ROS2 없이도 테스트 가능하게 만드는 것이 좋습니다.
#
# def detect_object(frame):
# return result
#
# 이렇게 만들면 카메라 파일, 웹캠, ROS2 Topic 어디서든 재사용 가능
#
# [ROS2와 연결되는 포인트]
# 실무 ROS2 비전 노드는 보통 다음 Topic을 가집니다.
#
# Subscribe:
# /camera/image_raw
#
# Publish:
# /vision/processed_image
# /vision/target_center
# /vision/detection_status
# ============================================================================
# 관련 기능과 데이터를 하나로 묶는 클래스를 정의함
class VisionNode(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드임
    def __init__(self):
        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 생성
        self.bridge = CvBridge()
        # image sub 변수에 이후 처리에 사용할 값을 저장
        self.image_sub = ...
        # image pub 변수에 이후 처리에 사용할 값을 저장
        self.image_pub = ...
        # result pub 변수에 이후 처리에 사용할 값을 저장
        self.result_pub = ...

    # image_callback 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def image_callback(self, msg):
        # 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        processed_frame, result = self.process_frame(frame)
        self.publish_image(processed_frame)
        self.publish_result(result)

    # process_frame 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def process_frame(self, frame):
        # OpenCV 처리
        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
        return processed_frame, result

    # publish_image 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def publish_image(self, processed_frame):
        # 처리 이미지 발행
        pass

    # publish_result 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def publish_result(self, result):
        # 좌표, 상태 등 발행
        pass
