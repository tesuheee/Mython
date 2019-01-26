import RPi.GPIO as GPIO
import time

stime = 0.1
pin = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)
while True:
    GPIO.output(pin, 1)
    time.sleep(stime)
    GPIO.output(pin, 0)
    time.sleep(stime)
GPIO.cleanup()
