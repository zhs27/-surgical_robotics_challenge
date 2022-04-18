# surgical_robotics_challenge

Project for CS 3891: Algorithms of Robotics. Goal is to implement the Da Vinci robot to perform needle work on ‚Äúpatient‚Äù.

## Task Briefdown

We break the task down into three parts:
1) Finding where the holes are: define global coordinate system; give global coordinates of the holes we are pushing the needle through and coordinate of the needle
2) Planning a trajectory: write a Action class with start point, end point, and type of movement (whether the push the needle through and in what direction); give a sequence of Actions
3) Carrying out movement: implement robot movement to actually push the needle through and move arm
 
## Find Needle Command
rostopic echo /ambf/env/Needle/State


