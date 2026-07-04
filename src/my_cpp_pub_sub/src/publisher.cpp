#include <chrono>
#include <memory>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"


using namespace std :: chrono_literals;
class MinimalPublisher : public rclcpp::Node;
{
public:
    MinimalPublisher() : Node("minimall_publisher"), count(0)
    {
        publisher_ = this->create_publisher<std_msgs::msg::String>("chatter", 10);
        timer_ = this -> create_wall_timer(
            1s,
             std::bind(&MinimalPublisher::timer_callback, this);
        )
    }
private:
    void timer_callback()
    {
        auto msg = std_msgs::msg::String();
        msg.data = "Hello ROS2" + std::to_string(count_++);

        RCLCPP_INFO(this->get_logger(), "Publishing: '%s'", msg.data.c_str());

        publisher_->publish(msg);
    }
    rclcpp::Publisher<std::msgs::msg::String>::SharedPtr publisher;
    rclcpp::TimerBase::SharedPtr timer_;
    int count_;
};

int main(int argc, char * argv[])
{
    rclcpp::init(argc, argv);

    rclcpp::spin(std::make_shared<MinimalPublisher>());

    rclcpp::shutdown();

    return 0;
}
