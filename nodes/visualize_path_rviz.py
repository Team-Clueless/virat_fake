#!/usr/bin/env python

import rospy
from virat_msgs.msg import Path
from geometry_msgs.msg import Point
from visualization_msgs.msg import MarkerArray, Marker
import sys


PATH_TOPIC = sys.argv[1]

VISUAL_TOPIC = sys.argv[2]

POINT_R, POINT_G, POINT_B, POINT_A = map(float, sys.argv[3].split())

LINE_R, LINE_G, LINE_B, LINE_A = map(float, sys.argv[4].split())


class Mark:
    def __init__(self):
        self.sub = rospy.Subscriber(PATH_TOPIC, Path, self.callback)

        self.pub = rospy.Publisher(VISUAL_TOPIC, MarkerArray, queue_size=10)

        self.markers = MarkerArray()

    def callback(self, path_msg):
        xs, ys = path_msg.x_vals, path_msg.y_vals

        for i, (x, y) in enumerate(zip(xs, ys)):

            marker = Marker()
            marker.header.frame_id = "/odom"
            marker.type = marker.SPHERE
            marker.action = marker.ADD
            marker.scale.x = 0.2
            marker.scale.y = 0.2
            marker.scale.z = 0.2
            marker.color.r = POINT_R
            marker.color.g = POINT_G
            marker.color.b = POINT_B
            marker.color.a = POINT_A
            marker.pose.orientation.w = 1.0
            marker.pose.position.x = x
            marker.pose.position.y = y
            marker.pose.position.z = 0

            self.markers.markers.append(marker)

        id = 0

        for m in self.markers.markers:
            m.id = id
            id += 1

        for j in range(i):

            start = Point()
            start.x, start.y, start.z = xs[j], ys[j], 0

            end = Point()
            end.x, end.y, end.z = xs[j + 1], ys[j + 1], 0

            line = Marker()
            line.id = id + j + 1
            line.header.frame_id = "/odom"
            line.type = line.LINE_STRIP
            line.action = line.ADD
            line.pose.orientation.w = 1.0
            line.scale.x = 0.1

            line.color.r = LINE_R
            line.color.g = LINE_G
            line.color.b = LINE_B
            line.color.a = LINE_A

            line.points.append(start)
            line.points.append(end)

            self.markers.markers.append(line)

        self.pub.publish(self.markers)
        self.markers = MarkerArray()


def main():
    rospy.init_node("rviz_path_marker", anonymous=False)
    _ = Mark()
    print("Node : %s active !!" % (rospy.get_name()))
    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException:
        pass
