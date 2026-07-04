#ifndef FLEET_MONITOR_HPP
#define FLEET_MONITOR_HPP

#include "rclcpp/rclcpp.hpp"
class FleetMonitor : public rclcpp::Node
{
public:
    FleetMonitor();

private:
    void timerCallback();

    rclcpp::TimerBase::SharedPtr timer_;
};

#endif