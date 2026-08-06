"""예제 85. 카메라 노드 구조 설계

Notion 강의 자료의 실습 소스를 파일로 분리한 예제입니다.
프로젝트 루트에서 실행하세요.
"""

class VisionNode(Node):
    def __init__(self):
        self.bridge = CvBridge()
        self.image_sub = ...
        self.image_pub = ...
        self.result_pub = ...

    def image_callback(self, msg):
        frame = self.bridge.imgmsg_to_cv2(msg, "bgr8")
        processed_frame, result = self.process_frame(frame)
        self.publish_image(processed_frame)
        self.publish_result(result)

    def process_frame(self, frame):
        # OpenCV 처리
        return processed_frame, result

    def publish_image(self, processed_frame):
        # 처리 이미지 발행
        pass

    def publish_result(self, result):
        # 좌표, 상태 등 발행
        pass
