"""
# This is a simple program for driving the servo motors
# open the lid of the respective trash cans on the 
# raspberry pi control unit.
# The default uses pin 12 and 13 for two servos
# 
# ===========================================
# Author: J. Jerry Cheng;
# ENGR-2050, Section 4, Team A, Summer 2020;
# Last Update 2020.07.23

"""


import time
import RPi.GPIO as GPIO


def sweep_servo(pwm_item, lid_time):
    # helper function, sweep the servo from 0
    # degrees to +90 and return to 0 degree after
    # lid_time.
    # 2in: GPIO.PWM, int; 0out;

    # opening the lid # 0->+90
    for dc in range(60, 81, 1):
        pwm_item.ChangeDutyCycle(dc)
        time.sleep(0.1)

    # maintain open
    time.sleep(lid_time)

    # closing the lid # +90->0
    for dc in range(80, 61, -1):
        pwm_item.ChangeDutyCycle(dc)
        time.sleep(0.1)
    return 

def open_lid(trash_type, lid_time=5):
    # packaged function, input the trashtype as string 
    # and open the respective lid.
    # available trash type: "plastic", "paper";
    # 2in: str, int(DEFAULT); 0out;  
    
    # pin_out
    PWM_PIN0 = 12
    PWM_PIN1 = 13

    # initial setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(PWM_PIN0, GPIO.OUT)
    GPIO.setup(PWM_PIN1, GPIO.OUT)
    
    pwm0 = GPIO.PWM(PWM_PIN0, 400) # 400 Hz, 2.5 ms signal duration 
    pwm1 = GPIO.PWM(PWM_PIN1, 400)

    # start pwm at 0 degree position (in the middle)
    # servo running with 
    # 1.5 ms pulse at 0 degree # respective duty cycle 1.5/2.5 = 60
    # ~1 ms pulse at -90 degree # respective duty cycle 1.0/2.5 = 40
    # ~2 ms pulse at +90 degree # respective duty cycle 2.0/2.5 = 80

    pwm0.start(60) # in the middle
    pwm1.start(60) # in the middle

    if trash_type.lower() == "plastic":
        sweep_servo(pwm0, lid_time)

    elif trash_type.lower() == "paper":
        sweep_servo(pwm1, lid_time)

    return

    
    