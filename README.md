# ev3_pathfinder
# Line Follower Robot with Obstacle Avoidance

This project implements a line-following robot using the LEGO EV3 Mindstorms kit. The robot can follow a black line and navigate around obstacles.

## Features
- **Line Following:** The robot follows a black line on the ground using a color sensor.
- **Obstacle Avoidance:** The robot detects obstacles using an ultrasonic sensor and navigates around them.

## Hardware Components
- **LEGO EV3 Brick:** The main control unit.
- **2 Large Motors:** To control the wheels of the robot.
- **Color Sensor:** To detect the black line.
- **Ultrasonic Sensor:** To detect obstacles.
- **Wheels and Chassis:** To build the robot structure.

## Installation
1. Ensure you have the `ev3dev2` library installed on your LEGO EV3 brick.
2. Clone this repository to your local machine.

    ```sh
    git clone https://github.com/singhadwika/ev3_pathfinder.git
    ```

3. Navigate to the project directory.

    ```sh
    cd line-follower-robot
    ```

4. Upload the Python script to your LEGO EV3 brick.

## Usage
1. Turn on your LEGO EV3 brick.
2. Run the script on the EV3 brick.

    ```sh
    ./line_follower_robot.py
    ```

3. Place the robot on a surface with a black line and ensure there are obstacles in its path to see the obstacle avoidance in action.
4. Press any button on the EV3 brick to stop the robot.

## Code Explanation
The main components of the script include:
- **Button and Sensor Initialization:** Initializes the buttons and sensors used in the project.
- **Motor Initialization:** Sets up the motors for controlling the wheels.
- **Main Function (`line_follower_robot`):** Contains the main logic for line following and obstacle avoidance.
- **Obstacle Avoidance Function (`avoid_obstacle`):** Contains hardcoded movements to navigate around obstacles.
- **Utility Functions:** 
  - `turn_left(duration)`: Function to turn the robot left.
  - `turn_right(duration)`: Function to turn the robot right.
  - `move_straight(duration)`: Function to move the robot straight.
