import RPi.GPIO as GPIO
import time

# constants
SERVO_1 = 11
SERVO_2 = 13
CLOSED_FREQ = 10
CLOSED_CDC = 1.5
OPEN_CCW = 0.8
OPEN_CW = 2.1
WAIT_TIME = 1

# globals
door_1 = None
door_2 = None


def init():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(SERVO_1, GPIO.OUT)
    GPIO.setup(SERVO_2, GPIO.OUT)
    global door_1
    global door_2
    door_1 = GPIO.PWM(SERVO_1, CLOSED_FREQ)
    door_2 = GPIO.PWM(SERVO_2, CLOSED_FREQ)
    door_1.start(CLOSED_CDC)
    door_2.start(CLOSED_CDC)


def main():
    init()
    try:
        while True:
            time.sleep(WAIT_TIME)
            door_1.ChangeDutyCycle(OPEN_CCW)
            door_2.ChangeDutyCycle(OPEN_CW)
            time.sleep(WAIT_TIME)
            door_1.ChangeDutyCycle(CLOSED_CDC)
            door_2.ChangeDutyCycle(CLOSED_CDC)
    except KeyboardInterrupt:
        GPIO.cleanup()
main()

