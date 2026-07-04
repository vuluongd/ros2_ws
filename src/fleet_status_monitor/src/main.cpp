#include "rclcpp/rclcpp.hpp"

int main(int argc, char *argv[]){
    rclcpp::init(argc, argv);

    auto node =  std::make_shared<rclcpp::Node>("fleet_monitor");

    RCLCPP_INFO(node->get_logger(), "Fleet Monitor Started");
    rclcpp::spin(node);
    rclcpp::shutdown();

    return 0;
}