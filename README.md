# surgical_robotics_challenge

Project for CS 3891: Algorithms of Robotics. Goal is to implement the Da Vinci robot to perform needle work on 'patient'.

## Task Breakdown

We break the task down into three parts:
1) Finding where the holes are: define global coordinate system; give global coordinates of the holes we are pushing the needle through and coordinate of the needle
2) Planning a trajectory: write a Action class with start point, end point, and type of movement (whether the push the needle through and in what direction); give a sequence of Actions
3) Carrying out movement: implement robot movement to actually push the needle through and move arm
 
## Find Needle Command
rostopic echo /ambf/env/Needle/State

## Code Structure

ambf should be at ~. So is surgical_robotics_challenge (https://github.com/collaborative-robotics/surgical_robotics_challenge.git)

## How to Run

1) start a terminal and run $roscore
2) start another terminal and run $~/ambf/bin/lin-x86_64/ambf_simulator --launch_file ~/surgical_robotics_challenge/launch.yaml -l 0,1,3,4,14,15 -p 120 -t 1 --override_max_comm_freq 120
