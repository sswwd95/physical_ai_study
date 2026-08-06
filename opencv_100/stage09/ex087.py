# ============================================================================
# 노션 원문 학습 설명: 예제 87. 실시간 Edge Publisher
# ============================================================================
#
# [핵심 주제]
# ROS2 카메라 이미지를 구독하고, Canny Edge를 적용한 결과 이미지를 다시 ROS2 Topic으로 발행
#
# [실습 목표]
# 1. Image Subscriber와 Publisher 동시 사용
# 2. Canny Edge 처리
# 3. mono8 이미지 발행
# 4. rqt_image_view로 결과 확인 가능한 구조 만들기
#
# [실무에서 자주 하는 실수]
# 실수 1. Edge 이미지를 bgr8로 발행
#
# Canny 결과는 1채널 이미지임
#
# 따라서 `mono8`으로 발행하는 것이 맞습니다.
#
# 실수 2. header를 복사하지 않음
#
# 이미지 동기화나 TF 연계가 필요한 경우 header가 중요
#
# edge_msg.header = msg.header
#
# [ROS2와 연결되는 포인트]
# 이 예제는 “처리 이미지 Topic 발행”의 기본임
#
# 원본 카메라
# → OpenCV 처리
# → 결과 이미지 Topic 발행
# → rqt_image_view/RViz2 확인
# ============================================================================
# Python으로 ROS2 노드를 만들고 실행하기 위해 rclpy를 불러오기
import rclpy
# ROS2 노드 클래스를 만들 때 상속할 Node를 불러오기
from rclpy.node import Node
# ROS2에서 카메라 영상을 주고받는 Image 메시지 형식을 불러오기
from sensor_msgs.msg import Image
# ROS2 Image 메시지와 OpenCV 이미지 배열을 서로 변환하는 CvBridge를 불러오기
from cv_bridge import CvBridge
# OpenCV 기능 사용을 위한 cv2 모듈 불러오기
import cv2

# 관련 기능과 데이터를 하나로 묶는 클래스를 정의함
class EdgePublisher(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드임
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정함
        super().__init__("edge_publisher")

        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 생성
        self.bridge = CvBridge()

        # 다른 ROS2 노드가 보낸 메시지를 받을 Subscriber를 생성
        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

        # 처리 결과를 다른 ROS2 노드에 보낼 Publisher를 생성
        self.edge_pub = self.create_publisher(
            Image,
            "/vision/edge_image",
            10
        )

    # image_callback 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def image_callback(self, msg):
        # 영상 변환이나 처리 중 오류가 나더라도 노드 전체가 갑자기 종료되지 않도록 예외 처리를 시작함
        try:
            # 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            # edge image 변수에 이후 처리에 사용할 값을 저장
            edge_image = self.process_frame(frame)

            # OpenCV 이미지 배열을 ROS2 Image 메시지로 변환
            edge_msg = self.bridge.cv2_to_imgmsg(
                edge_image,
                encoding="mono8"
            )

            edge_msg.header = msg.header

            # 완성한 ROS2 메시지를 지정한 Topic으로 발행
            self.edge_pub.publish(edge_msg)

        # 위의 처리 과정에서 오류가 발생했을 때 실행할 코드를 작성함
        except Exception as e:
            # 오류 내용을 ROS2 로그에 출력
            self.get_logger().error(f"Edge 처리 오류: {e}")

    # process_frame 작업을 반복해서 사용할 수 있도록 함수로 정의함
    def process_frame(self, frame):
        # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 가운데 픽셀에 더 큰 가중치를 주는 가우시안 블러를 적용
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)

        # 두 개의 임계값을 사용하는 Canny 알고리즘으로 안정적인 경계선을 찾습니다.
        edges = cv2.Canny(blurred, 50, 150)

        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료
        return edges

# 프로그램 실행 순서를 담당하는 main 함수를 정의함
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장
    node = EdgePublisher()

    # 노드가 종료될 때까지 콜백을 계속 처리하도록 실행 상태를 유지
    rclpy.spin(node)

    # 사용이 끝난 ROS2 노드 자원을 정리함
    node.destroy_node()
    # ROS2 사용을 종료하고 관련 자원을 정리함
    rclpy.shutdown()

# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인
if __name__ == "__main__":
    main()
