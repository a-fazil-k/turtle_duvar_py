import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math

class KacanKaplumbaga(Node):
    def __init__(self):
        super().__init__('kacan_kaplumbaga')
        self.declare_parameter('ileri_hiz', 3.0)
        self.declare_parameter('alt_sinir', 1.0)
        self.declare_parameter('ust_sinir', 10.0)
        
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        self.subscriber_ = self.create_subscription(Pose, '/turtle1/pose', self.pose_callback, 10)
        self.timer_ = self.create_timer(1.0, self.log_callback)
        
        self.current_x = 5.5
        self.current_y = 5.5
        self.current_theta = 0.0
        
        self.hedef_aci = 0.785
        self.donuyor = True

    def pose_callback(self, msg):
        self.current_x = msg.x
        self.current_y = msg.y
        self.current_theta = msg.theta
        
        hiz = self.get_parameter('ileri_hiz').get_parameter_value().double_value
        alt = self.get_parameter('alt_sinir').get_parameter_value().double_value
        ust = self.get_parameter('ust_sinir').get_parameter_value().double_value
        
        cmd = Twist()
        
        if not self.donuyor:
            carpma = False
            sag_duvar = (self.current_x > ust) and (math.cos(self.current_theta) > 0)
            sol_duvar = (self.current_x < alt) and (math.cos(self.current_theta) < 0)
            ust_duvar = (self.current_y > ust) and (math.sin(self.current_theta) > 0)
            alt_duvar = (self.current_y < alt) and (math.sin(self.current_theta) < 0)
            
            if sag_duvar or sol_duvar:
                self.hedef_aci = math.pi - self.current_theta
                carpma = True
            if ust_duvar or alt_duvar:
                self.hedef_aci = -self.current_theta
                carpma = True
                
            if carpma:
                self.donuyor = True
                self.hedef_aci = math.atan2(math.sin(self.hedef_aci), math.cos(self.hedef_aci))

        if self.donuyor:
            aci_farki = math.atan2(math.sin(self.hedef_aci - self.current_theta), math.cos(self.hedef_aci - self.current_theta))
            if abs(aci_farki) > 0.1:
                cmd.linear.x = 0.0
                cmd.angular.z = 5.0 if aci_farki > 0 else -5.0
            else:
                self.donuyor = False
                cmd.linear.x = hiz
                cmd.angular.z = 0.0
        else:
            cmd.linear.x = hiz
            cmd.angular.z = 0.0
            
        self.publisher_.publish(cmd)

    def log_callback(self):
        self.get_logger().info(f'X: {self.current_x:.2f}, Y: {self.current_y:.2f}')

def main(args=None):
    rclpy.init(args=args)
    node = KacanKaplumbaga()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
