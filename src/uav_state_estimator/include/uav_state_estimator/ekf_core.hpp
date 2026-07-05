#ifndef EKF_CORE_HPP_
#define EKF_CORE_HPP_

#include <Eigen/Dense>
#include <Eigen/Geometry>
#include <vector>
#include <cmath>

namespace uav_state_estimator{
class EKFcore{
public:
    EKFcore();
    ~EKFcore() = default;

    void setInitialState(const Eigen::VectorXd& x0, const Eigen::MatrixXd& P0);
    
}
}