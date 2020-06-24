#include <ros/ros.h>
#include <virat_msgs/Path.h>
#include <virat_msgs/MPC_EstStates.h>

class FakePathPlanner
{

private:
    virat_msgs::Path fake_path; // message to publish

    ros::Publisher pub;
    ros::Subscriber sub;

public:
    FakePathPlanner(ros::NodeHandle *nh)
    {

        this->pub = nh->advertise<virat_msgs::Path>("/virat/fake/path", 10);

        this->sub = nh->subscribe("/virat/controller/input/state", 100, &FakePathPlanner::callback, this);
    }

    void callback(const virat_msgs::MPC_EstStates::ConstPtr &msg)
    {
        boost::array<double, 10ul> xs = {0};
        boost::array<double, 10ul> ys;

        double inc = 2;

        for (int i = 0; i < 10; i++)
        {
            xs[i] = i * i * 0.1;
            ys[i] = 10 - inc * i;
        }

        this->fake_path.x_vals = xs;
        this->fake_path.y_vals = ys;
        // publish fake path
        this->pub.publish(this->fake_path);
        ROS_INFO("Sending fake target trajectory to controller");
    }
};

int main(int argc, char **argv)
{
    ros::init(argc, argv, "fake_path_planner");
    ros::NodeHandle nh;

    FakePathPlanner fake = FakePathPlanner(&nh);

    ROS_INFO("\n\nPublishing fake path in topic    : /virat/fake/path\n");

    ros::spin();

    return 0;
}
