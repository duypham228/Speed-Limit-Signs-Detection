# Capstone_Speed_Limit_Classification

Created by Duy Pham, Ian Stephenson, Sophia Stutes, and Bao Vo for CSCE 482 Capstone, Spring 2022.

AutoDrive Challenge 2022

## How it works
In this project, Robotic Operating Systems 2 (ROS2) is used to take in images of speed limit signs, classify them, and then produce output for the user to view, which will contain the digit classified by the model.

#### In order to run this project:

1. Open a Terminal via a Linux-based system. This can be in Linux OS, Windows Subsystem for Linux (WSL), Docker, etc.

2. Navigate to the dev_ws folder (via 'cd' commands).

3. Run the command: **rosdep install -i --from-path src --rosdistro foxy -y**
* This command will install any dependencies and ROS materials needed to run the code.
* This may take several minutes, depending on what you may already have installed or not.

4. Run the command: **colcon build**
* This command will build the ROS package. 
* This will produce a few lines of output if successful.

5. Open a NEW Terminal window, and navigate to the dev_ws directory. This will be terminal "alpha".

6. Run the command: **. install/setup.bash**
* Note: no terminal output will be produced.

7. Repeat steps 5 and 6 once more, which will open up a third Terminal window. This third terminal will be terminal "beta".

8. In terminal alpha, run this command: **ros2 run ros2_speed_limit image_file**
* This will run the publisher, which accesses the image files and publishes the data from the files elsewhere.
* This will produce terminal output indicating the file location of the image.

9. In terminal beta, run this command: **ros2 run ros2_speed_limit classifier**.
* This will run the subscriber and classifier, which takes the published image data and classifies the numerical value. 
* This will produce terminal output indicating the numerical value detected, or a print-out statement if no image could be found.

This next part is optional, but may be wanting to be done if you wish to see what the classifier publishes. 

10. Complete steps 5 and 6 once again. This fourth terminal window will be called "delta".

11. Take terminal delta and run this command: **ros2 run ros2_speed_limit listener**. 
* You will now be able to see what the classifier is publishing, outside of the classifier's connected terminal itself. 
