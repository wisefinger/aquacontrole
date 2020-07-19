print("start pump program.....................")
#import RPi.GPIO as GPIO
import time
from datetime import datetime

# define input port relay 1
relay1 = 32
# define input port relay 2
relay2 = 0
# define input port relay 3
relay3 = 0
# define input port relay 4
relay4 = 0
teller = 1

now = datetime.now()
current_time = now.strftime("%H:%M:%S")


# current_time = now.strftime("%D %H:%M:%S")

def init():
    global teller
    #print(f"test:{teller}")
    teller += 0


    # set number method for using GPIO lib
    # GPIO.setmode(GPIO.BOARD)
    # configure pin number for relay switch     no spaces after the comma
    #GPIO.setup(relay1, GPIO.OUT)
    # set pin to high
    #GPIO.output(relay1, GPIO.HIGH)
    # to set time


#def waterchange(duration):
    # Activate relay/pump
    #GPIO.output(relay1, GPIO.LOW)
    #time to keep relay on
    #print("Current time =", current_time)
    #time.sleep(duration)
    # start initialisation


# init()
# time.sleep(2)

# if(current time =

#waterchange(5)

# to reset all the pins
# GPIO.cleanup()

#print(".....................end pump program")
#exit()