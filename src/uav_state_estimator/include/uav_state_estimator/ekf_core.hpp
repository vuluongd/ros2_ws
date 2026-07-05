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
    void predict(double dt, const Eigen::Vector3d& gyro, const Eigen::Vector3d& acc);
    void updateGPS(const Eigen::Vector3d& pos, const Eigen::Vector3d& vel = Eigen::Vector3d::Zero());

    Eigen::VectorXd getState const  {return x_;}
    Eigen::MatrixXd getCovariance const {return P_;}

    // Get position, velocity, attitude (quaternion)

    Eigen::Vector3d getPosition() const { return x_.segment<3>(0); }
    Eigen::Vector3d getVelocity() const { return x_.segment<3>(3); }
    Eigen::Quaterniond getAttitude() const {
        Eigen::Quaterniond q(x_(6), x_(7), x_(8), x_(9));
        q.normalize();
        return q;
    }
private:
     // State and covariance
    Eigen::VectorXd x_; //16*1
    Eigen::MatrixXd P_;  //16*16

     // Noise covariance matrices
     Eigen::MatrixXd Q_;  
     Eigen::MatrixXd R_;

     // Helper functions
     Eigen::MatrixXd computeStateTransitionJacobian(double dt);
     Eigen::MatrixXd computeProcessNoiseCovariance(double dt);
     Eigen::MatrixXd computeMeasurementJacobian(double dt);
     Eigen::VectorXd computeMeasurementPrediction();

     Eigen::Quaterniond quaternionFromVec(const Eigen::Vector3d& v);
     Eigen::Vector3d quaternionRotate(const Eigen::Quaterniond& q, const Eigen::Vector3d& v);
};

}
#endif  // EKF_CORE_HPP_