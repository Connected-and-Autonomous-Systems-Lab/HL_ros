import rclpy
from rclpy.node import Node

from std_msgs.msg import String
import socket
from colorama import init, Fore
import struct
from geometry_msgs.msg import Pose

# Initialize colorama
init()

# Define host and port
HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server


class Imu_publisher(Node):

    def __init__(self):
        super().__init__('imu_publisher')
        self.publisher_ = self.create_publisher(Pose, 'pose', 10)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the server
            s.connect((HOST, PORT))
            print(Fore.GREEN + 'Connected to the hl2ss')
            # Receive messages from the server indefinitely
            while True:
                data = s.recv(1024)  # Receive up to 1024 bytes of data
                if not data:
                    break
                
                head_position =  data.decode()
                print(head_position)
                head_position = list(map(float,head_position.strip('[]').split()))
                print(Fore.WHITE + "Received From socket:", head_position)
                pose = Pose()

                pose.position.x = head_position[0]
                pose.position.y = head_position[1]
                pose.position.z = head_position[2]
                self.publisher_.publish(pose)


def main(args=None):
    rclpy.init(args=args)

    imu_publisher = Imu_publisher()

    rclpy.spin(imu_publisher)

    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    imu_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()