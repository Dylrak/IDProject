#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import time
from Database_verification import getNFCUID
import threading

# constants for GPIO
SERVO_1 = 11
SERVO_2 = 13
GREEN_LIGHT = 8
YELLOW_LIGHT = 10
RED_LIGHT = 12
# Constants for PWM
CLOSED_FREQ = 10
CLOSED = 1.5
OPEN_CCW = 2.1
OPEN_CW = 0.8
WAIT_TIME = 0.5

class GateProcess(threading.Thread):  # Process to authenticate user, then open and close gates
    # global within gateProcess
    door_1 = None
    door_2 = None

    def __init__(self, threadName):
        threading.Thread.__init__(self)
        self.name = threadName

    def run(self, is_ingang):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SERVO_1, GPIO.OUT)
        GPIO.setup(SERVO_2, GPIO.OUT)
        GPIO.setup(GREEN_LIGHT, GPIO.OUT)
        GPIO.setup(YELLOW_LIGHT, GPIO.OUT)
        GPIO.setup(RED_LIGHT, GPIO.OUT)
        global door_1
        global door_2
        global OPEN_CCW
        global OPEN_CW
        if is_ingang:
            OPEN_CCW = 0.8
            OPEN_CW = 2.1
        door_1 = GPIO.PWM(SERVO_1, CLOSED_FREQ)
        door_2 = GPIO.PWM(SERVO_2, CLOSED_FREQ)
        door_1.start(CLOSED)
        door_2.start(CLOSED)
        GPIO.output(RED_LIGHT, 1)
        uID = getNFCUID()
        if self.authenticated(uID):
            self.openDoors()
        GPIO.cleanup()


    def openDoors(self):
        door_1.ChangeDutyCycle(OPEN_CCW)
        door_2.ChangeDutyCycle(OPEN_CW)
        GPIO.output(RED_LIGHT, 0)
        GPIO.output(GREEN_LIGHT, 1)
        time.sleep(WAIT_TIME * 4)  # Wait 2 seconds
        GPIO.output(GREEN_LIGHT, 0)
        yellow_on = False
        for i in range(0, 6):  # For the next 3 seconds, flash yellow light
            yellow_on = not yellow_on
            GPIO.output(YELLOW_LIGHT, yellow_on)
            time.sleep(WAIT_TIME)
        door_1.ChangeDutyCycle(CLOSED)  # CLOSE THE GAAAATES!!!
        door_2.ChangeDutyCycle(CLOSED)
        GPIO.output(RED_LIGHT, 1)
        time.sleep(WAIT_TIME)

    def authenticated(self, uID):
        return True