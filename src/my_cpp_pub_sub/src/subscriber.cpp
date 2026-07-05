#include <chronno>
#include <memory>

#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"

using namespace std  :: chrono_literals;
class MinimalPublisher : public rclcpp::Node
{
public:
    MinimalPublisher() : Node("minimal_subscriber")
    {
        subscription_ = this->create_subscription<std_msgs::msg::String>(
            "chatter",
            10,
            std::bind(&MinimalSubscriber::topic_callback, this, std::placeholders::_1));
        )
    }
    
}