#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import time
import MFRC522
import signal

# constants for GPIO(/PWM)
SERVO_1 = 11
SERVO_2 = 13
CLOSED_FREQ = 10
CLOSED_CDC = 1.5
OPEN_CCW = 0.8
OPEN_CW = 2.1
NOCHANGE = 0
WAIT_TIME = 2

exitProcess = False


class GateProcess:  # Process to open and close gates
    # global within gateProcess
    door_1 = None
    door_2 = None

    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SERVO_1, GPIO.OUT)
        GPIO.setup(SERVO_2, GPIO.OUT)
        global door_1
        global door_2
        door_1 = GPIO.PWM(SERVO_1, CLOSED_FREQ)
        door_2 = GPIO.PWM(SERVO_2, CLOSED_FREQ)
        door_1.start(CLOSED_CDC)
        door_2.start(CLOSED_CDC)
        uID = self.getNFCUID()
        if self.authenticated(uID):
            door_1.ChangeDutyCycle(OPEN_CCW)
            door_2.ChangeDutyCycle(OPEN_CW)
            time.sleep(WAIT_TIME)
            door_1.ChangeDutyCycle(CLOSED_CDC)
            door_2.ChangeDutyCycle(CLOSED_CDC)
            time.sleep(WAIT_TIME)

    def openDoors(self):
        GPIO.cleanup()

    def authenticated(self, uID):
        return True

    def getNFCUID(self):
        continue_reading = True

        # Capture SIGINT for cleanup when the script is aborted
        def end_read(uid):
            global continue_reading
            print "uID is: %s,%s,%s,%s" % (str(uid[0]), str(uid[1]), str(uid[2]), str(uid[3]))
            continue_reading = False

        # Hook the SIGINT
        signal.signal(signal.SIGINT, end_read)

        # Create an object of the class MFRC522
        MIFAREReader = MFRC522.MFRC522()
        while continue_reading:
            # Scan for cards
            (status, TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)

            # If a card is found
            if status == MIFAREReader.MI_OK:
                print
                "Card detected"

            # Get the UID of the card
            (status, uid) = MIFAREReader.MFRC522_Anticoll()

            # If we have the UID, return it and clean up.
            if status == MIFAREReader.MI_OK:
                end_read(uid)
                return uid
               
GateProcess()
