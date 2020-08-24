#script for testing the replay board
import time
import RPi.GPIO as GPIO

# set number method for using GPIO lib
GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)
# configure pin number for relay switch     no spaces after the comma
GPIO.setup(32, GPIO.OUT)
# set pin to high
GPIO.output(32, GPIO.HIGH)
    
    
GPIO.output(32, GPIO.LOW)
# time to keep relay on
time.sleep(10)
    
GPIO.cleanup()

 