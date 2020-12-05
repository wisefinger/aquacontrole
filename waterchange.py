#script for testing the replay board
import time
from datetime import datetime, timedelta
import RPi.GPIO as GPIO
GPIO.setwarnings(True)
# set number method for using GPIO lib
GPIO.setmode(GPIO.BOARD)
# configure pin number for relay switch     no spaces after the comma
GPIO.setup(32, GPIO.OUT)

print(f' start watercycle :{datetime.now().strftime("%d/%m/%Y:%X")}')
# set pin to high
GPIO.output(32, GPIO.LOW)
# time to keep relay on
# 5 minutes is about 27 liters
time.sleep(5* 60)
GPIO.output(32, GPIO.HIGH)
print(f' stop watercycle :{datetime.now().strftime("%d/%m/%Y:%X")}')


    
GPIO.cleanup()