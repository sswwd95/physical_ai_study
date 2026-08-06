"""예제 86. 이미지 Subscriber 구조

초보자용 상세 주석판입니다.

읽는 순서:
1. 위에서 아래로 주석을 먼저 읽습니다.
2. 바로 아래 코드가 어떤 작업을 하는지 확인합니다.
3. 실행 후 나타나는 창이나 터미널 결과를 비교합니다.

실행 위치: 이 프로젝트의 opencv_100 폴더
주의: cv2.imshow()가 있는 예제는 화면 창에서 아무 키나 눌러야 종료됩니다.
"""

# Python으로 ROS2 노드를 만들고 실행하기 위해 rclpy를 불러옵니다.
import rclpy
# ROS2 노드 클래스를 만들 때 상속할 Node를 불러옵니다.
from rclpy.node import Node
# ROS2에서 카메라 영상을 주고받는 Image 메시지 형식을 불러옵니다.
from sensor_msgs.msg import Image
# ROS2 Image 메시지와 OpenCV 이미지 배열을 서로 변환하는 CvBridge를 불러옵니다.
from cv_bridge import CvBridge
# OpenCV 기능을 사용하기 위해 cv2 모듈을 불러옵니다.
import cv2

# 관련 기능과 데이터를 하나로 묶는 클래스를 정의합니다.
class BasicVisionSubscriber(Node):
    # 객체가 만들어질 때 한 번 실행되는 초기화 메서드입니다.
    def __init__(self):
        # 부모 Node 클래스의 초기화 기능을 실행하고 이 ROS2 노드의 이름을 정합니다.
        super().__init__("basic_vision_subscriber")

        # ROS2 이미지와 OpenCV 이미지 사이를 변환할 CvBridge 객체를 만듭니다.
        self.bridge = CvBridge()

        # 다른 ROS2 노드가 보낸 메시지를 받을 Subscriber를 만듭니다.
        self.image_sub = self.create_subscription(
            Image,
            "/camera/image_raw",
            self.image_callback,
            10
        )

    # image_callback 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
    def image_callback(self, msg):
        # 영상 변환이나 처리 중 오류가 나더라도 노드 전체가 갑자기 종료되지 않도록 예외 처리를 시작합니다.
        try:
            # 수신한 ROS2 Image 메시지를 OpenCV에서 처리할 수 있는 NumPy 배열로 변환합니다.
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                desired_encoding="bgr8"
            )

            # processed frame 변수에 이후 처리에 사용할 값을 저장합니다.
            processed_frame = self.process_frame(frame)

            # 처리 결과를 확인할 수 있도록 별도의 OpenCV 창에 이미지를 표시합니다.
            cv2.imshow("Processed Frame", processed_frame)
            # 키 입력을 기다립니다. 값이 작으면 실시간 영상이 계속 갱신됩니다.
            cv2.waitKey(1)

        # 위의 처리 과정에서 오류가 발생했을 때 실행할 코드를 작성합니다.
        except Exception as e:
            # 오류 내용을 ROS2 로그에 출력합니다.
            self.get_logger().error(f"이미지 처리 오류: {e}")

    # process_frame 작업을 반복해서 사용할 수 있도록 함수로 정의합니다.
    def process_frame(self, frame):
        # BGR 컬러 이미지를 밝기 정보만 있는 흑백 이미지로 변환합니다.
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # 이미지를 필요한 색상 공간으로 변환합니다.
        processed_frame = cv2.cvtColor(
            gray,
            cv2.COLOR_GRAY2BGR
        )

        # 함수의 처리 결과를 호출한 위치로 돌려주고 함수를 종료합니다.
        return processed_frame

# 프로그램 실행 순서를 담당하는 main 함수를 정의합니다.
def main(args=None):
    # ROS2 통신을 사용할 수 있도록 rclpy를 초기화합니다.
    rclpy.init(args=args)

    # node 변수에 이후 처리에 사용할 값을 저장합니다.
    node = BasicVisionSubscriber()

    # 노드가 종료될 때까지 콜백을 계속 처리하도록 실행 상태를 유지합니다.
    rclpy.spin(node)

    # 사용이 끝난 ROS2 노드 자원을 정리합니다.
    node.destroy_node()
    # OpenCV가 만든 모든 이미지 창을 닫습니다.
    cv2.destroyAllWindows()
    # ROS2 사용을 종료하고 관련 자원을 정리합니다.
    rclpy.shutdown()

# 이 파일을 직접 실행했을 때만 main 함수를 호출하도록 확인합니다.
if __name__ == "__main__":
    main()
