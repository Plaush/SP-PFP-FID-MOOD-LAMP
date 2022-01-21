# CODE BY NATASHA
from microbit import *  # import the main microbit code
from servo import Servo  # import the servo lib for servo functions
from random import randint  # import random lib for rand gen function

redVal = 0
greenVal = 0
blueVal = 0
# Declaring variables

Servo_pin = pin0
servo = Servo(Servo_pin)
servo.write_angle(0)
# Assigning Servo Pins

while True:
    if button_a.was_pressed():
        greenVal = randint(100, 255)  # Randomly picks a green value
        redVal = randint(100, 255)  # Randomly picks a red value
        blueVal = randint(100, 255)  # Randomly picks a blue value
        pin1.write_analog(redVal)  # Assigns value to pin
        pin2.write_analog(greenVal)  # Assigns value to pin
        pin12.write_analog(blueVal)  # Assigns value to pin
# Random light value generator

    if button_b.was_pressed():
        pin1.write_digital(0)  # Assign a value of '0'/Off to pin
        pin2.write_digital(0)  # Assign a value of '0'/Off to pin
        pin12.write_digital(0)  # Assign a value of '0'/Off to pin
        sleep(1000)
# Turns off light
    if button_a.is_pressed() and button_b.is_pressed():
        # Requires two buttons to be held
        while True:
            servo.write_angle(90)  # Motor rotates 90 degrees
            sleep(800)
            sleep.write_angle(0)
            # Motor returns to origin (Don't want to over strain the wires)
# Operates Servo
