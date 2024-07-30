#!/usr/bin/env python3
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1
from ev3dev2.sensor.lego import ColorSensor, UltrasonicSensor
from ev3dev2.button import Button
from time import sleep

# Initialize the button for stopping the program
btn = Button() 

# Initialize the color sensor and set it to reflection mode
cl = ColorSensor()
cl.mode = 'COL-REFLECT'

# Initialize the ultrasonic sensor and set it to measure distance in centimeters
us = UltrasonicSensor()
us.mode = 'US-DIST-CM'

# Initialize the motors
motor_left = LargeMotor(OUTPUT_A)
motor_right = LargeMotor(OUTPUT_B)

# Initialize a MoveTank object to control both motors simultaneously
motors = MoveTank(OUTPUT_A, OUTPUT_B)

# Define a constant for the timing when searching for the black line
timing_search = 0.5

def line_follower_robot():
    try:
        while not btn.any():  # Loop until a button is pressed
            if us.value() < 100:  # Check if an obstacle is within 10 cm
                avoid_obstacle()  # Navigate around the obstacle

            if cl.value() < 25:  # Check if the color sensor detects black
                motor_left.run_forever(speed_sp=200)  # Move forward
                motor_right.run_forever(speed_sp=200)  # Move forward
            else:  # If the color sensor does not detect black
                motors.off()  # Stop the motors
                sleep(0.1)  # Wait for a short period

    except Exception as e:
        print(e)

def avoid_obstacle():
    # Function to navigate around an obstacle
    turn_left(0.3)
    move_straight(0.7)
    turn_right(0.3)
    move_straight(0.5)
    turn_right(0.3)

    while cl.value() >= 25:  # Continue moving until the black line is detected
        motors.on(SpeedPercent(50), SpeedPercent(50))

    turn_left(0.3)  # Adjust back to the line

def turn_left(duration):
    # Function to turn the robot left
    motors.on_for_seconds(SpeedPercent(-50), SpeedPercent(50), duration)

def turn_right(duration):
    # Function to turn the robot right
    motors.on_for_seconds(SpeedPercent(50), SpeedPercent(-50), duration)

def move_straight(duration):
    # Function to move the robot straight
    motors.on_for_seconds(SpeedPercent(50), SpeedPercent(50), duration)

line_follower_robot()

# Stop the motors at the end of the program
motor_left.stop(stop_action='brake')
motor_right.stop(stop_action='brake')
