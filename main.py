import RPi.GPIO as GPIO
import threading
import time

# constants for GPIO(/PWM)
SERVO_1 = 11
SERVO_2 = 13
CLOSED_FREQ = 10
CLOSED_CDC = 1.5
OPEN_CCW = 0.8
OPEN_CW = 2.1
WAIT_TIME = 1

exitProcess = False


class GateProcess(threading.Thread):
    # global within gateProcess
    door_1 = None
    door_2 = None

    def __init__(self):
        threading.Thread.__init__(self)
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(SERVO_1, GPIO.OUT)
        GPIO.setup(SERVO_2, GPIO.OUT)
        global door_1
        global door_2
        door_1 = GPIO.PWM(SERVO_1, CLOSED_FREQ)
        door_2 = GPIO.PWM(SERVO_2, CLOSED_FREQ)
        door_1.start(CLOSED_CDC)
        door_2.start(CLOSED_CDC)

    def run(self):
        while not exitProcess:
            time.sleep(WAIT_TIME)
            door_1.ChangeDutyCycle(OPEN_CCW)
            door_2.ChangeDutyCycle(OPEN_CW)
            time.sleep(WAIT_TIME)
            door_1.ChangeDutyCycle(CLOSED_CDC)
            door_2.ChangeDutyCycle(CLOSED_CDC)
        GPIO.cleanup()
        self.name.exit()


class TestProcess(threading.Thread):
    def __init(self):
        threading.Thread.__init__(self)
        
    def run(self):
        try:
            global exitProcess
        except KeyboardInterrupt:
            exitProcess = True
gateThread = GateProcess()
testThread = TestProcess()
gateThread.start()
testThread.start()
