# Requirements

* ROS
* gazebo
* ros-kortex

You can acces a guideline for this installations (https://docs.google.com/presentation/d/1P1K28ihcsm6FGJCooZQ1cktJAYDkpnXx6-GcI8w_n1M/edit?usp=sharing)



# How to run the experiments

* Download or clone the repository in ROS repository workspace/src/ros-kortex
* Open a terminal and run ` roslaunch kortex_gazebo spawn_kortex_robot.launch`
* Open another terminal and run ` rosrun experiments_poc1 *.py`,where * is one of the scripts for example, main.py
