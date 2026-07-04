#include "fleet_status_monitor/fleet_monitor.hpp"
#include <functional>

using namespace std :: chrono_literals;

FleetMonitor::FleetMonitor()
:Node("fleet_monitor")
{
    RCLCPP_INFO(get_logger(), "Fleet Monitor Started!");
    
    timer_ = create_wall_timer(
        1s,
        std::bind(&FleetMonitor::timerCallback, this)
    );
}

void FleetMonitor::timerCallback()
{
    RCLCPP_INFO(get_logger(), "FLEET IS ALIVE....");
}