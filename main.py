import RPi.GPIO as GPIO
import time

#constants
SERVO_1 = 11
SERVO_2 = 13
CLOSED_FREQ = 10
CLOSED_CDC = 1.5
OPEN_CCW = 0.8
OPEN_CW = 2.1
WAIT_TIME = 1

GPIO.setmode(GPIO.BOARD)
GPIO.setup(SERVO_1,GPIO.OUT)
GPIO.setup(SERVO_2, GPIO.OUT)
pwm_1 = GPIO.PWM(SERVO_1, CLOSED_FREQ)
pwm_2 = GPIO.PWM(SERVO_2, CLOSED_FREQ)
pwm_1.start(CLOSED_CDC)
pwm_2.start(CLOSED_CDC)
while True:
    time.sleep(WAIT_TIME)
    pwm_1.ChangeDutyCycle(OPEN_CCW)
    pwm_2.ChangeDutyCycle(OPEN_CW)
    time.sleep(WAIT_TIME)
    pwm_1.ChangeDutyCycle(CLOSED_CDC)
    pwm_2.ChangeDutyCycle(CLOSED_CDC)
