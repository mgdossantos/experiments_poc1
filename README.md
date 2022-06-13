# Requirements

* ROS
* gazebo
* ros-kortex

You can acces a guideline for this installations (https://docs.google.com/presentation/d/1P1K28ihcsm6FGJCooZQ1cktJAYDkpnXx6-GcI8w_n1M/edit?usp=sharing)

# How to setup the tools

* Go to catkin_workspace/src
* Execute the command source /devel/setup.bash
* Create a package using catkin_create_pkg experiments_poc1 rospy
* Download or clone the repository experiments_poc1 in ROS repository workspace/src/ros-kortex
* Copy all the sub-folder from folder experiments_poc1/assests/models to your gazebo folder
* Replace the file spawn_kortex_robot.launch on folder ros_kortex/kortex_gazebo/launch/ for the version on this repository 
* Copy the folder worlds on this repository to ros_kortex/kortex_gazebo
* Go to catkin_workspace/src and run the command catkin_make 

# How to run the experiments

* Open a terminal and run ` roslaunch kortex_gazebo spawn_kortex_robot.launch`
* Open another terminal and run ` rosrun experiments_poc1 *.py`,where * is one of the scripts for example, main.py
