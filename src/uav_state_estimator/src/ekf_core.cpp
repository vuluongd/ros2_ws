#include "uav_state_estimator/ekf_core.hpp"
#include <iostream>

namespace uav_state_estimator {
EkfCore::EkfCore(){
    x_ = Eigen::VectorXd::Zero(16);
    x_(6) = 1.0;

    // Covariance: large initial uncertainty for position/velocity, small for biases

    P_ = Eigen::MatrixXd::zero(12,12);
    P_.block<3,3>(0,0) *= 10.0; // position
    P_.block<3,3>(3,3) *= 10.0; // velocity
    P_.block<3,3>(6,6) *= 0.01; // attitude (small)
    P_.block<3,3>(10,10) *= 0.1; // accel bias
    P_.block<3,3>(13,13) *= 0.1; //gyro bias

     // Process noise (IMU)

     Q_ = Eigen::MatrixXd::Zero(12,12);
     


}

}