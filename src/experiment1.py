#!/usr/bin/env python3

import sys
import rospy
import time
from kortex_driver.srv import *
from kortex_driver.msg import *
from RobotActions import ExampleCartesianActionsWithNotifications

testarm = ExampleCartesianActionsWithNotifications()


def goHome(testarm):
	testarm.example_home_the_robot()
	feedback = rospy.wait_for_message("/" + testarm.robot_name + "/base_feedback", BaseCyclic_Feedback)
	

def goPointA(testarm):
	feedback = rospy.wait_for_message("/" + testarm.robot_name + "/base_feedback", BaseCyclic_Feedback)
	testarm.example_send_cartesian_pose(0,0.2,0,0,0,0)
	testarm.example_send_cartesian_pose(0,0,0,80,0,0)
	testarm.example_send_cartesian_pose(0,0,-0.29,0,0,0)
	

def goPointB(testarm):
	feedback = rospy.wait_for_message("/" + testarm.robot_name + "/base_feedback", BaseCyclic_Feedback)
	
	testarm.example_send_cartesian_pose(0,0,0,0,0,80)
	testarm.example_send_cartesian_pose(0,0.45,0,0,0,0)
	testarm.example_send_cartesian_pose(-0.9,0,0,0,0,0)
	testarm.example_send_cartesian_pose(0,0,-0.5,0,0,0)
	
	
def goPointC(testarm):
	
	testarm.example_send_cartesian_pose(0,0,0.5,0,0,0)
	

def closeGripper(testarm):
    testarm.example_send_gripper_command(1)


def openGripper(testarm):
    testarm.example_send_gripper_command(0)


if __name__ == "__main__":

	success = testarm.is_init_success
	openGripper(testarm)
	goHome(testarm)
	goPointA(testarm)
	closeGripper(testarm)
	goHome(testarm)
	goPointB(testarm)
	openGripper(testarm)
	goPointC(testarm)
	goHome(testarm)
	
