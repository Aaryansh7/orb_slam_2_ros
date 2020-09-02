#! /usr/bin/env python3

import rospy
from geometry_msgs.msg import PoseStamped
import time

class SavePoses(object):
    def __init__(self):
        
        self.time_step=0
        self.x=0.0
        self.y=0.0
        self.z=0.0

    def pose_callback(self, msg):
        
        self.x = msg.pose.position.x + -2.7890250785779287
        self.y = msg.pose.position.y + -5.003651750117708
        self.z = msg.pose.position.z +  1.8768916811284049
    
    def write_to_file(self):

        sub_pose=rospy.Subscriber('/orb_slam2_mono/pose',PoseStamped,self.pose_callback,queue_size=1)
        self.time_step+=1   
        print("x:   "+str(self.x))
        print("y:   "+str(self.y))
        print("z:   "+str(self.z))
        #print("time: "+ str(self.time_step))        
        file.write(str(self.time_step) + ':\n----------\n' + "pose.x: " + str(self.x) +'\n' + "pose.y: " + str(self.y) +'\n' + "pose.z: " + str(self.z)  + '\n===========\n')
                    

if __name__ == "__main__":


    rospy.init_node('Poseprint', log_level=rospy.INFO) 
    save_spots_object = SavePoses()
    with open('poses.txt', 'w') as file:

        while not rospy.is_shutdown():
            save_spots_object.write_to_file()
            rospy.Rate(11).sleep()
