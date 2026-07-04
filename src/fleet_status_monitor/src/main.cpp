#include "fleet_status_monitor/fleet_monitor.hpp"


int main(int argc, char *argv[])
{
    rclcpp::init(argc, argv);

    auto node = std::make_shared<FleetMonitor>();

    rclcpp::spin(node);

    rclcpp::shutdown();

    return 0;
}