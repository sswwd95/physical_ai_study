"""예제 85. 카메라 노드 구조 설계

초보자용 상세 주석판입니다.

읽는 순서:
1. 위에서 아래로 주석을 먼저 읽습니다.
2. 바로 아래 코드가 어떤 작업을 하는지 확인합니다.
3. 실행 후 나타나는 창이나 터미널 결과를 비교합니다.

실행 위치: 이 프로젝트의 opencv_100 폴더
주의: cv2.imshow()가 있는 예제는 화면 창에서 아무 키나 눌러야 종료됩니다.
"""

# 관련 기능과 데이터를 하나로 묶는 클래스를 정의합니다.
class VisionNode(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드입니다.
    def __init__(self):
        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 만듭니다.
        self.bridge = CvBridge()
        # image sub 변수에 이후 처리에 사용할 값을 저장합니다.
        self.image_sub = ...
        # image pub 변수에 이후 처리에 사용할 값을 저장합니다.
        self.image_pub = ...
        # result pub 변수에 이후 처리에 사용할 값을 저장합니다.
        self.result_pub = ...

    # image_callback 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
    def image_callback(self, msg):
        # 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환합니다.
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        processed_frame, result = self.process_frame(frame)
        self.publish_image(processed_frame)
        self.publish_result(result)

    # process_frame 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
    def process_frame(self, frame):
        # OpenCV 처리
        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료합니다.
        return processed_frame, result

    # publish_image 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
    def publish_image(self, processed_frame):
        # 처리 이미지 발행
        pass

    # publish_result 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
    def publish_result(self, result):
        # 좌표, 상태 등 발행
        pass
